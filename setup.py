"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from pathlib import Path
from setuptools import setup, find_packages


with open(Path(__file__).parent / "LICENSE") as f:
    LICENSE_CT = f.read()


setup(
    name="ensembl-variation-graphql",
    description="GraphQL Ariadne-based prototype for Ensembl Variation",
    version="0.1.0",
    packages=find_packages(),
    license=LICENSE_CT,
    python_requires=">=3.8",
    package_data={
        # Make sure schema makes it to distro
        "common": ["*.graphql"]
    },
)
