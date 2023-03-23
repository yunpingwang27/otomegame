# VNDB Thigh-highs dumps helpers

## Tag
```
from vndb_thigh_highs.dumps import TagDatabaseBuilder

builder = TagDatabaseBuilder()

tag_database = builder.build_with_json_file("path/to/tags.json")
# or
tag_database = builder.build_with_archive("path/to/tags.json.gz")

tag = tag_database.get_tag(tag_id)
```

## Trait
```
from vndb_thigh_highs.dumps import TraitDatabaseBuilder

builder = TraitDatabaseBuilder()

trait_database = builder.build_with_json_file("path/to/traits.json")
# or
trait_database = builder.build_with_archive("path/to/traits.json.gz")

trait = trait_database.get_trait(traid_id)
```

## Votes
```
from vndb_thigh_highs.dumps import VoteBuilder

builder = VoteBuilder()

votes = builder.build_with_text_file("path/to/votes.txt")
# or
votes = builder.build_with_archive("path/to/votes.gz")
```
