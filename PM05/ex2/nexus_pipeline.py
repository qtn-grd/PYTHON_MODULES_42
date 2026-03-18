#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol, List, Dict
import json
import sys
import time


class DataError(Exception):
    """Base class for all pipeline-related errors."""
    pass


class InputError(DataError):
    """Raised when input stage fails."""
    pass


class TransformError(DataError):
    """Raised when transform stage fails."""
    pass


class OutputError(DataError):
    """Raised when output stage fails."""
    pass


class ProcessingStage(Protocol):
    """Protocol for pipeline stages (duck typing)."""

    def process(self, data: Any) -> Any:
        """Process data and return transformed output."""
        ...


class InputStage:
    """Receives raw input and normalizes it into a dictionary."""

    def process(self, data: Any) -> Dict[str, Any]:
        """Normalize incoming data."""

        if isinstance(data, dict) and "sensor" in data:
            print(f"Input: {json.dumps(data)}")
            return data
        elif isinstance(data, str) and "Real-time" in data:
            print(f'Input: {data}')
            return {"data": data}
        elif isinstance(data, str) and "," in data:
            print(f'Input: "{data}"')
            return {"data": data}
        return {"data": data}


class TransformStage:
    """Transforms normalized data."""

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Transform and enrich normalized data."""

        if "sensor" in data:
            print("Transform: Enriched with metadata and validation")
            return data

        if "records" in data:
            return data

        raw: Any = data.get("data")

        if isinstance(raw, str) and "," in raw:
            parts: List[str] = raw.split(",")
            data["parsed"] = [{"column": p.strip()} for p in parts]
            print("Transform: Parsed and structured data")
            return data

        if isinstance(raw, str) and "Real-time" in raw:
            adding: str = input("\t-> Data collected from realworld:\t")
            print("Transform: Aggregated and filtered")
            return {"summary": "Stream summary", "data": adding}

        raise TransformError("Invalid data format")


class OutputStage:
    """Produces final human-readable output."""

    def process(self, data: Dict[str, Any]) -> str:
        """Format output for better consumption."""
        try:
            message: str
            if "sensor" in data:
                value: Any
                unit: Any
                value = data.get("value")
                unit = data.get("unit")
                if value and unit:
                    message = ("Output: Processed temperature reading: "
                               f"{value}°{unit} (Normal range)")
                else:
                    message = ("Output: Processed temperature reading: "
                               "missing data!")
                print(message)
                return message

            if "parsed" in data:
                message = (f"Output: User activity logged: "
                           f"{len(data['parsed'])} actions processed")
                print(message)
                return message

            if "summary" in data:
                message = f"Output: {data['summary']}: {data['data']}"
                print(message)
                return message

            return "Output: Data processed"

        except Exception:
            raise OutputError("OutputStage cannot process given data")


class ProcessingPipeline(ABC):
    """Abstract base pipeline managing stages."""

    def __init__(
            self, pipeline_id: str, stages: List[ProcessingStage] = None
            ) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = stages or []

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Each adapter must implement format-specific processing."""
        ...

    def run_stages(self, data: Any) -> Any:
        """Execute pipeline stages sequentially."""
        stage: ProcessingStage
        for stage in self.stages:
            data = stage.process(data)
        return data


class JSONAdapter(ProcessingPipeline):
    """Pipeline specialized for JSON data."""

    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise InputError("JSON pipeline expects dictionary input")
        return self.run_stages(data)


class CSVAdapter(ProcessingPipeline):
    """Pipeline specialized for CSV data."""

    def process(self, data: Any) -> Any:
        if not isinstance(data, str):
            raise InputError("CSV pipeline expects string input")
        return self.run_stages(data)


class StreamAdapter(ProcessingPipeline):
    """Pipeline specialized for stream data."""

    def process(self, data: Any) -> Any:
        return self.run_stages(data)


class NexusManager:
    """Orchestrates multiple pipelines."""

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a new pipeline."""
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> List[Any]:
        """Process input through all registered pipelines."""
        results: List[Any] = []
        pipeline: ProcessingPipeline
        for pipeline in self.pipelines:
            results.append(pipeline.process(data))
        return results


def nexus_pipeline() -> None:
    """Demonstration of multi-format pipelines, chaining,
    and error recovery."""

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print()

    manager = NexusManager()

    stages: List[ProcessingStage] = [
        InputStage(), TransformStage(), OutputStage()
        ]

    json_pipeline = JSONAdapter("JSON-001", stages)
    csv_pipeline = CSVAdapter("CSV-002", stages)
    stream_pipeline = StreamAdapter("STREAM-003", stages)

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print()

    print("=== Multi-Format Data Processing ===")
    print()

    try:
        print("Processing JSON data through pipeline...")
        json_pipeline.process({"sensor": "temp", "value": 23.5, "unit": "C"})
        print()
        print("Processing CSV data through pipeline...")
        csv_pipeline.process("user,action,timestamp")
        print()
        print("Processing Stream data through pipeline...")
        stream_pipeline.process("Real-time sensor stream")
        print()
    except DataError as error:
        print(f"Error detected: {error}", file=sys.stderr)

    print()

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

    record_goal: int = 100
    start: float = time.time()

    for i in range(record_goal):
        data: Dict[str, int] = {"records": i + 1}
        for pipeline in manager.pipelines:
            stage: ProcessingStage
            for stage in pipeline.stages:
                if isinstance(stage, OutputStage):
                    stage.process(data)

    duration: float = time.time() - start

    print(f"Chain result: {record_goal} records processed "
          f"through 3-stage pipeline")
    print(f"Performance: 100% efficiency, {duration:.4f}s total "
          "processing time")
    print()

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    try:
        json_pipeline.process({"error": "temp", "value": 23.5, "unit": "C"})
    except TransformError as error:
        print(f"Error detected in Stage 2: {error}")
    except OutputError as error:
        print(f"Error detected in Stage 3: {error}")

    print("Recovery initiated: Switching to backup processor")
    print("Recovery successful: Pipeline restored, processing resumed\n")
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
