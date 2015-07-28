# Copyright 2015 NEC Corporation
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
SQLAlchemy models for inspection data.
"""

from oslo_db.sqlalchemy import models
from sqlalchemy import Column, Float, ForeignKey, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(cls=models.ModelBase)


class Node(Base):
    __tablename__ = 'nodes'
    uuid = Column(String(36), primary_key=True)
    started_at = Column(Float, nullable=True)
    finished_at = Column(Float, nullable=True)
    error = Column(Text, nullable=True)


class Attribute(Base):
    __tablename__ = 'attributes'
    name = Column(Text, primary_key=True)
    value = Column(Text, primary_key=True)
    uuid = Column(String(36), ForeignKey('nodes.uuid'))


class Option(Base):
    __tablename__ = 'options'
    uuid = Column(String(36), ForeignKey('nodes.uuid'), primary_key=True)
    name = Column(Text, primary_key=True)
    value = Column(Text)