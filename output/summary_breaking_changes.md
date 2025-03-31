Summary:

Here is a summary of the changes between versions 410 and 450:

* The Trino community released several major updates with significant breaking changes, improvements, and new features.
* The major changes can be grouped into several categories:
 + Breaking changes in data formats and serialization (e.g., removal of support for late materialization, null-suppression from RowBlock fields, and deprecation of legacy table statistics tracking).
 + Changes in configuration properties and session variables (e.g., renaming of query.max-writer-tasks-count to query.max-writer-task-count, disallowing invalid configuration options, and removing support for legacy create-table-with-existing-location).
 + Improvements in performance (e.g., caching data on local storage, improving aggregations containing a DISTINCT clause, and optimizing scan parallelism in BigQuery).
 + New features and improvements (e.g., addition of required ConnectorSession parameter to the method TableFunctionProcessorProvider.getDataProcessor, enablement of bigquery.arrow-serialization.enabled by default, and support for V2 of the Nessie REST API).
 + Updates to Trino's dependencies and libraries (e.g., removal of support for Phoenix versions 5.1.x and earlier, update Glue to V2 REST interface).

Some specific breaking changes include:

* Removal of support for late materialization
* Removal of null-suppression from RowBlock fields
* Renaming of query.max-writer-tasks-count to query.max-writer-task-count
* Disallowing invalid configuration options
* Removal of legacy create-table-with-existing-location
* Removal of support for split size configuration with the catalog properties delta.max-initial-splits and delta.max-initial-split-size
* Removal of deprecated legacy materialized-view-grace-period configuration property
* Removal of deprecated PARTITION_COLUMN and PARTITION_VALUE arguments from the flush_metadata_cache procedure
