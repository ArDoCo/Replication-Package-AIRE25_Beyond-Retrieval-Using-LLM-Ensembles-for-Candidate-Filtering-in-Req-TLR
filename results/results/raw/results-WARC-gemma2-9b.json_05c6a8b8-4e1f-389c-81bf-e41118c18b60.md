## Configuration (2025-06-02_17-59+0200 -- WARC-gemma2-9b.json_05c6a8b8-4e1f-389c-81bf-e41118c18b60)
```json
{
  "cache_dir" : "./cache-r2r/WARC-ensemble",
  "gold_standard_configuration" : {
    "hasHeader" : true,
    "path" : "./datasets/req2req/WARC/answer.csv",
    "swap_columns" : false
  },
  "source_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/WARC/high"
    }
  },
  "target_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/WARC/low"
    }
  },
  "source_preprocessor" : {
    "name" : "artifact",
    "args" : { }
  },
  "target_preprocessor" : {
    "name" : "artifact",
    "args" : { }
  },
  "embedding_creator" : {
    "name" : "mock",
    "args" : { }
  },
  "source_store" : {
    "name" : "custom",
    "args" : { }
  },
  "target_store" : {
    "name" : "custom",
    "args" : {
      "max_results" : "infinity"
    }
  },
  "classifiers" : [ [ {
    "name" : "simple_ollama",
    "args" : {
      "model" : "gemma2:9b",
      "seed" : "133742243",
      "template" : "Question: Here are two parts of software development artifacts.\n\n{source_type}: '''{source_content}'''\n\n{target_type}: '''{target_content}'''\nAre they related?\n\nAnswer with 'yes' or 'no'.\n"
    }
  } ] ],
  "result_aggregator" : {
    "name" : "any_connection",
    "args" : {
      "source_granularity" : "0",
      "target_granularity" : "0"
    }
  },
  "tracelinkid_postprocessor" : {
    "name" : "req2req",
    "args" : { }
  }
}
```

## Stats
* #TraceLinks (GS): 136
* #Source Artifacts: 63
* #Target Artifacts: 89
## Results
* True Positives: 136
* False Positives: 4782
* False Negatives: 0
* Precision: 0.027653517690117934
* Recall: 1.0
* F1: 0.05381875741986545
