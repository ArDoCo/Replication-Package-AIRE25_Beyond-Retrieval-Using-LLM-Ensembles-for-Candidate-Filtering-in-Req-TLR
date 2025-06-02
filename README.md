# Replication Package for "Beyond Retrieval: A Study of Using LLM Ensembles for Candidate Filtering in Requirements Traceability"
by Dominik Fuchß, Stefan Schwedt, Jan Keim, and Tobias Hey

This is the replication package for our paper "Beyond Retrieval: A Study of Using LLM Ensembles for Candidate Filtering in Requirements Traceability".
This package contains the source code, the dataset used in the evaluation, and the results of the evaluation.

## Requirements
- Java JDK 21 + Maven 3
- Open AI subscription: API Key
- Ollama Instance

## Structure of this Repository
* `/` contains the source code of the approach (Note: The most recent version of the tool can be found at [ArDoCo/LiSSA-RATLR](https://github.com/ArDoCo/LiSSA-RATLR))
* `/cache-r2r` contains the cache for the evaluation.
* `/configs` contains the configurations used in the evaluation.
* `/datasets` contains the datasets used in the evaluation and the results of the evaluation.
* `/results` contains the results of the evaluation.

## Installation
a. You can use the provided JAR.
b. You can build the project using Maven using `mvn package` . The Jar will be created in the target folder in the project (target/ratlr-*-jar-with-dependencies.jar).

## Usage
1. Create a `.env` file based on the template
2. Run the jar from the toplevel directory, e.g., `java -jar target/ratlr-*-jar-with-dependencies.jar eval -c ./configs/req2req/<<DesiredConfig>>`

# Results of Evaluation
You will find all our results in the `results` folder. The results are stored as MD files in the respective projects.
It contains the configuration and the results of the evaluation.
It could look like the following:

```
## Configuration

{
  "cache_dir" : "./cache/CCHIT",
  "gold_standard_configuration" : {
    "hasHeader" : true,
    "path" : "./datasets/req2req/CCHIT/answer.csv"
  },
  "source_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/CCHIT/high"
    }
  },
  "target_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/CCHIT/low"
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
    "name" : "openai",
    "args" : {
      "model" : "text-embedding-3-large"
    }
  },
  "source_store" : {
    "name" : "custom",
    "args" : { }
  },
  "target_store" : {
    "name" : "custom",
    "args" : {
      "max_results" : "4"
    }
  },
  "classifier" : {
    "name" : "mock",
    "args" : { }
  },
  "result_aggregator" : {
    "name" : "any_connection",
    "args" : {
      "source_granularity" : "0",
      "target_granularity" : "0"
    }
  },
  "tracelinkid_postprocessor" : {
    "name" : "identity",
    "args" : {
      "reverse" : "false"
    }
  }
}

## Stats
* # TraceLinks (GS): 587
* # Source Artifacts: 116
* # Target Artifacts: 1064
## Results
* True Positives: 92
* False Positives: 372
* False Negatives: 495
* Precision: 0.19827586206896552
* Recall: 0.1567291311754685
* F1: 0.17507136060894388
```
