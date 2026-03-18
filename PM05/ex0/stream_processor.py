#!/usr/bin/env python3


from typing import Any, List, Union, Dict
from abc import ABC, abstractmethod
import sys


class ProcessorError(Exception):
    """Base exception for all processors."""
    pass


class NumericError(ProcessorError):
    """Exception raised for numeric processing errors."""
    pass


class TextError(ProcessorError):
    """Exception raised for text processing errors."""
    pass


class LogError(ProcessorError):
    """Exception raised for log processing errors."""
    pass


class DataProcessor(ABC):
    """An abstract base class defining the common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a formatted string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string. Can be overridden by subclasses."""
        return result


class NumericProcessor(DataProcessor):
    """Processor for numeric data (int or float, single or list)."""

    def validate(
            self, data: Union[int, float, list[Union[int, float]]]) -> bool:
        """Validate if data is appropriate for this processor."""

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(elem, (int, float)) for elem in data)

        return False

    def process(self, data: Union[int, float, list[Union[int, float]]]) -> str:
        """Process the data and return result stringpass."""

        if not self.validate(data):
            raise NumericError("Invalid numeric data")

        try:
            numbers: List[Union[int, float]]

            if isinstance(data, (int, float)):
                numbers = [data]
            else:
                numbers = data

            count: int = len(numbers)
            total: float = sum(numbers)
            average: float = total / count

            return (
                f"Processed {count} numeric values, "
                f"sum={total}, avg={average}"
            )

        except Exception as error:
            raise NumericError(f"Processing error: {error}")

    def format_output(self, result: str) -> str:
        """Override format_output to allow some specialization."""

        specif: str = "NUMERIC"
        return f"{specif} ~ {super().format_output(result)}"


class TextProcessor(DataProcessor):
    """Processor for text data (str or list of str)."""

    def validate(self, data: Union[str, list[str]]) -> bool:
        """Validate if data is appropriate for this processor."""

        if isinstance(data, str):
            return True

        if isinstance(data, list) and all(isinstance(s, str) for s in data):
            return True

        return False

    def process(self, data: Union[str, list[str]]) -> str:
        """Process the data and return result stringpass."""

        if not self.validate(data):
            raise TextError("Invalid text data")

        try:
            if isinstance(data, list):
                text: str = " ".join(data)
            else:
                text: str = data

            charac_count: int = len(text)
            word_count: int = len(text.split())

            return (
                f"Processed text: {charac_count} characters, "
                f"{word_count} words"
            )

        except Exception as error:
            raise TextError(f"Processing error: {error}")

    def format_output(self, result: str) -> str:
        """Override format_output to allow some specialization."""

        specif: str = "TEXT"
        return f"{specif} ~ {super().format_output(result)}"


class LogProcessor(DataProcessor):
    """Processor for log data (single string)."""

    def validate(self, data: str) -> bool:
        """Validate if data is appropriate for this processor."""

        return isinstance(data, str)

    def process(self, data: str) -> str:
        """Process the data and return result stringpass."""

        if not self.validate(data):
            raise LogError("Invalid log data")

        level: str
        message: str

        try:
            if ": " not in data:
                level = "INFO"
                message = data
                tags: Dict[str, str] = "[INFO]"
            else:
                level, message = data.split(": ", 1)
                level = level.upper()

                tags: Dict[str, str] = {
                    "ERROR": "[ALERT]",
                    "INFO": "[INFO]",
                    "WARNING": "[WARN]"
                }

                tag: str = tags.get(level, "[INFO]")

            return f"{tag} {level} level detected: {message}"

        except Exception as error:
            raise LogError(f"Processing error : {error}")

    def format_output(self, result: str) -> str:
        """Override format_output to allow some specialization."""

        specif: str = "LOG"
        return f"{specif} ~ {super().format_output(result)}"


def stream_processor() -> str:
    """Demo function showing individual and polymorphic processing."""

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    numeric_test: list[int] = [1, 2, 3, 4, 5]
    text_test: str = "Hello Nexus World"
    log_test: str = "ERROR: Connection timeout"

    print("Initializing Numeric Processor...")

    try:
        print(f"Processing data: {numeric_test}")
        if NumericProcessor().validate(numeric_test):
            print("Validation: Numeric data verified")
        numeric_output: str = NumericProcessor().format_output(
            NumericProcessor().process(numeric_test))
        print(numeric_output)
    except ProcessorError as error:
        print(f"ERROR: {error}", file=sys.stderr)

    print()
    print("Initializing Text Processor...")

    try:
        print(f'Processing data: "{text_test}"')
        if TextProcessor().validate(text_test):
            print("Validation: Text data verified")
        text_output: str = TextProcessor().format_output(
            TextProcessor().process(text_test))
        print(text_output)
    except ProcessorError as error:
        print(f"ERROR: {error}", file=sys.stderr)

    print()
    print("Initializing Log Processor...")

    try:
        print(f'"Processing data: "{log_test}"')
        if LogProcessor().validate(log_test):
            print("Validation: Log data verified")
        log_output: str = LogProcessor().format_output(
            LogProcessor().process(log_test))
        print(log_output)
    except ProcessorError as error:
        print(f"ERROR: {error}", file=sys.stderr)

    print()
    print("=== Polymorphic Processing Demo ===")
    print()

    datas_list: list[tuple[Any, DataProcessor]] = [
        ([1, 2, 3], NumericProcessor()),
        ("Hello Nexus!", TextProcessor()),
        ("INFO: System ready", LogProcessor())
    ]
    print("Processing multiple data types through same interface...")

    for elem, (data, processor) in enumerate(datas_list, start=1):

        try:
            result: str = processor.process(data)
            output: str = processor.format_output(result)
            print(f"Result {elem}: {output}")
        except ProcessorError as error:
            print(f"Result {elem}: ERROR - {error}", file=sys.stderr)

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
