from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    def operate(self, text: str = None, params: Dict = None) -> str:
        text = text.strip()
        words = text.split()
        initials = [word[0].upper() + '.' for word in words]
        return ' '.join(initials)

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize