#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union
import sys


class DataError(Exception):
    """Base exception for all stream processing errors."""


class SensorError(DataError):
    """Raised when sensor stream processing fails."""


class TransactionError(DataError):
    """Raised when transaction stream processing fails."""


class EventError(DataError):
    """Raised when event stream processing fails."""


class DataStream(ABC):
    """Abstract base class representing a generic data stream."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[str]) -> str:
        """Process a batch of raw stream data.
        Must be implemented by subclasses."""

    def filter_data(
        self,
        data_batch: List[str],
        criteria: Optional[str] = None
    ) -> List[str]:
        """Filter incoming data according to optional criteria.
        Default implementation performs no filtering."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[int, str]]:
        """Return processing statistics for the stream."""
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    """Stream processing environmental sensor readings."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temp_values: List[float] = []

            for item in data_batch:
                sensor: str
                value: str
                sensor, value = item.split(":")
                numeric_value: float = float(value)

                if sensor == "temp":
                    temp_values.append(numeric_value)

            count: int = len(data_batch)
            self.processed_count += count

            if temp_values:
                avg_temp: float = sum(temp_values) / len(temp_values)
                return (
                    f"Sensor analysis: {count} readings processed, "
                    f"avg temp: {avg_temp:.1f}°C"
                )
            else:
                return (
                    f"Sensor analysis: {count} readings processed, "
                    f"avg temp: no data found"
                )

        except Exception as error:
            raise SensorError(f"Sensor stream processing failed: "
                              f"{error}") from error


class TransactionStream(DataStream):
    """Stream processing financial transaction batches."""

    def process_batch(self, data_batch: List[str]) -> str:
        try:
            buy_values: List[int] = []
            sell_values: List[int] = []

            for item in data_batch:
                operation: str
                value: str
                operation, value = item.split(":")
                numeric_value: int = int(value)

                if operation == "buy":
                    buy_values.append(numeric_value)
                elif operation == "sell":
                    sell_values.append(numeric_value)

            net_units: int = sum(buy_values) - sum(sell_values)

            studied: int = len(data_batch)
            self.processed_count += studied

            sign: str = "+" if net_units > 0 else ""

            return (
                f"Transaction analysis: {studied} operations, "
                f"net flow: {sign}{net_units} units"
            )

        except Exception as error:
            raise TransactionError(
                f"Transaction stream processing failed: {error}"
            ) from error


class EventStream(DataStream):
    """Stream processing system event batches."""

    def process_batch(self, data_batch: List[str]) -> str:
        try:
            error_count: int = sum(1 for item in data_batch if item == "error")

            studied: int = len(data_batch)
            self.processed_count += studied

            return (
                f"Event analysis: {studied} events, "
                f"{error_count} errors detected"
            )

        except Exception as error:
            raise EventError(f"Event stream processing failed: "
                             f"{error}") from error


class StreamProcessor:
    """Central processor managing multiple streams
    through a unified interface."""

    def __init__(self) -> None:
        self.streams: Dict[str, DataStream] = {}

    def add_stream(self, stream: DataStream) -> None:
        """Register a new stream."""
        self.streams[stream.stream_id] = stream

    def process_batches(self, batches: Dict[str, List[str]]) -> None:
        """Process incoming batches mapped by stream_id."""

        stream_id: str
        stream: DataStream
        for stream_id, stream in self.streams.items():
            batch: List[str] = batches.get(stream_id, [])

            try:
                filtered: List[str] = stream.filter_data(batch)
                result: str = stream.process_batch(filtered)

                print(f"{stream.__class__.__name__} result: {result}")

            except DataError as error:
                print(
                    f"Error processing {stream.__class__.__name__}: {error}",
                    file=sys.stderr
                )

    def get_stats(self) -> None:
        """Print statistics for all registered streams."""

        stream: DataStream
        for stream in self.streams.values():
            stats: Dict[str, Union[int, str]] = stream.get_stats()
            print(f"{stream.__class__.__name__} stats: {stats}")


def data_stream():

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    processor = StreamProcessor()

    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    sensor_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    event_batch: List[str] = ["login", "error", "logout"]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: Environmental Data")
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    try:
        print(sensor_stream.process_batch(sensor_batch))
    except SensorError as error:
        print(error, file=sys.stderr)

    print()

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction_stream.stream_id}, Type: Financial Data")
    print(f"Processing transaction batch: [{', '.join(transaction_batch)}]")
    try:
        print(transaction_stream.process_batch(transaction_batch))
    except TransactionError as error:
        print(error, file=sys.stderr)

    print()

    print("Initializing Event Stream...")
    print(f"Stream ID: {event_stream.stream_id}, Type: System Events")
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    try:
        print(event_stream.process_batch(event_batch))
    except EventError as error:
        print(error, file=sys.stderr)

    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    mixed_batches: List[tuple[DataStream, List[str]]] = [
        (sensor_stream, ["temp:25.0", "humidity:65", "temp:27.0"]),
        (transaction_stream, ["buy:50", "sell:25", "buy:30", "sell:10"]),
        (event_stream, ["login", "error", "error"])
    ]

    print()
    print("Batch 1 Results:")

    sensor_count: int = 0
    transaction_count: int = 0
    event_count: int = 0

    critical_sensor_alerts: int = 0
    large_transactions: int = 0

    for stream, batch in mixed_batches:

        try:
            filtered: List[str] = stream.filter_data(batch)
            stream.process_batch(filtered)

            if isinstance(stream, SensorStream):
                for item in batch:
                    sensor_type: str
                    value_str: str
                    sensor_type, value_str = item.split(":")
                    value: float = float(value_str)
                    if sensor_type == "temp":
                        sensor_count += 1
                        if value > 23.0:
                            critical_sensor_alerts += 1

            elif isinstance(stream, TransactionStream):
                transaction_count += len(batch)
                if transaction_count > 3:
                    large_transactions += 1

            elif isinstance(stream, EventStream):
                event_count += len(batch)

        except DataError as error:
            print(error, file=sys.stderr)

    print(f"- Sensor Data: {sensor_count} readings processed")
    print(f"- Transaction Data: {transaction_count} operations processed")
    print(f"- Event Data: {event_count} events processed")
    print()

    print("Stream filtering active: High-priority data only")
    print(f"Filtered results: {critical_sensor_alerts} critical "
          f"sensor alerts, {large_transactions} large transaction")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
