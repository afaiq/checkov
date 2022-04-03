from typing import Dict, Any

from checkov.common.checks.base_check import BaseCheck
from checkov.common.models.enums import CheckResult

from checkov.openapi.checks.registry import openapi_registry as registry


class BaseOpenapiCheck(BaseCheck):
    def __init__(self, name, id, categories, supported_entities, block_type, path=None, guideline=None) -> None:
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_entities=supported_entities,
            block_type=block_type,
            guideline=guideline,
        )
        self.path = path
        registry.register(self)

    # def scan_entity_conf(self, conf: Dict[str, Any], entity_type: str) -> CheckResult:
        # self.entity_type = entity_type
        # self.scan_spec_cof(conf,entity_type)

    # @multi_signature()
    # @abstractmethod
    # def scan_spec_conf(self, conf: Dict[str, Any], entity_type: str) -> CheckResult:
    #     """Return result of Kubernetes object check."""
    #     raise NotImplementedError()
