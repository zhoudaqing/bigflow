#
# Copyright (c) 2015 Baidu, Inc. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
"""
Script Definition

"""
from bigflow import pcollection
from bigflow.transform_impls import reduce
from bigflow.util import utils


def min(pvalue, key=None):
    """
    Implementation of transforms.max()
    """
    if not isinstance(pvalue, pcollection.PCollection):
        raise ValueError("Invalid argument: pvalue must be of type PCollection")
    if utils.is_infinite(pvalue):
        raise ValueError("min not supported infinite PType")

    if key is None:
        return reduce.reduce(pvalue, lambda x, y: x if x < y else y)
    else:
        return reduce.reduce(pvalue, lambda x, y: x if key(x) < key(y) else y)
