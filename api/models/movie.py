from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute
)

class Movie(Model):

  class Meta:
    table_name = 'movies'
    host = "http://localhost:8000"
    write_capacity_units = 5
    read_capacity_units = 25

  title = UnicodeAttribute(hash_key=True)
  format = UnicodeAttribute()
  length = NumberAttribute()
  release_year = NumberAttribute(range_key=True)
  rating = NumberAttribute()

  def __iter__(self):
    for name, attr in self._get_attributes().items():
        yield name, attr.serialize(getattr(self, name))