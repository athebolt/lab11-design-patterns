from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    def operate(self, text: str = None, params: Dict = None) -> str:
        words = text.split()
        initials = []

        for word in words:
            initial = ""

            # Find the first alphanumeric character
            for char in word:
                if char.isalnum():
                    initial += char.upper() + '.'
                    initials.append(initial)
                    break
                initial += char
            else:
                # If no alphanumeric character, keep the word as is
                initials.append(word)

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