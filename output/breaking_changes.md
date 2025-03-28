# Breaking Changes Summary

## Version 432
[Release Notes](https://trino.io/docs/current/release/release-432.html)

Breaking changes:
* ⚠️ Breaking change: Remove support for late materialization, including the
experimental.late-materialization.enabled and
experimental.work-processor-pipelines configuration properties. (#19611)
* ⚠️ Breaking change: Remove null-suppression from RowBlock fields. Add new factory methods to
create a RowBlock, and remove the old factory methods. (#19479)

## Version 434
[Release Notes](https://trino.io/docs/current/release/release-434.html)

Breaking changes:
* ⚠️ Breaking change: Rename the query.max-writer-tasks-count configuration property
and the related max_writer_tasks_count session property to
query.max-writer-task-count and max_writer_task_count. (#19793)
* ⚠️ Breaking change: Disallow invalid configuration options. Previously, they were
silently ignored.  (#19735)
* ⚠️ Breaking change: Remove support for legacy table statistics tracking. (#19803)
* ⚠️ Breaking change: Disallow invalid configuration options. Previously, they were
silently ignored.  (#19735)
* ⚠️ Breaking change: Remove the VariableWidthBlockBuilder.buildEntry method. (#19577)
* ⚠️ Breaking change: Add required  ConnectorSession parameter to the method
TableFunctionProcessorProvider.getDataProcessor. (#19778)

## Version 435
[Release Notes](https://trino.io/docs/current/release/release-435.html)

Breaking changes:
* ⚠️ Breaking change: Remove support for registering external tables with
CREATE TABLE and the location table property. Use the
register_table procedure as replacement. The property
delta.legacy-create-table-with-existing-location.enabled is
also removed. (#17016)

## Version 436
[Release Notes](https://trino.io/docs/current/release/release-436.html)

Breaking changes:
* ⚠️ Breaking change: Require JDK 21.0.1 to run Trino, including updated
JVM config. (#20010)
* ⚠️ Breaking change: Add support for ElasticSearch
version 8,
and remove support for ElasticSearch version 6. (#20258)

## Version 437
[Release Notes](https://trino.io/docs/current/release/release-437.html)

Breaking changes:
* ⚠️ Breaking change: Replace the exchange.compression-enabled configuration property
and exchange_compression session property with
the exchange.compression-codecand exchange_compression_codec properties,
respectively. (#20274)
* ⚠️ Breaking change: Replace the spill-compression-enabled configuration property
with the spill-compression-codec property. (#20274)
* ⚠️ Breaking change: Remove the deprecated experimental.spill-compression-enabled
configuration property. (#20274)

## Version 439
[Release Notes](https://trino.io/docs/current/release/release-439.html)

Breaking changes:
* ⚠️ Breaking change: Improve performance of caching data on local storage. Deprecate
the hive.cache.enabled configuration property in favor of
fs.cache.enabled. (#20658, #20102)

## Version 440
[Release Notes](https://trino.io/docs/current/release/release-440.html)

Breaking changes:
* ⚠️ Breaking change: Remove the defunct *.http-client.max-connections properties.
(#20966)

## Version 441
[Release Notes](https://trino.io/docs/current/release/release-441.html)

Breaking changes:
* ⚠️ Breaking change: Remove the default legacy mode for the hive.security
configuration property, and change the default value to allow-all.
Additionally, remove the legacy properties hive.allow-drop-table,
hive.allow-rename-table, hive.allow-add-column, hive.allow-drop-column,
hive.allow-rename-column, hive.allow-comment-table, and
hive.allow-comment-column. (#21013)

## Version 444
[Release Notes](https://trino.io/docs/current/release/release-444.html)

Breaking changes:
* ⚠️ Breaking change: Remove support for split size configuration with the catalog
properties delta.max-initial-splits and delta.max-initial-split-size, and
the catalog session property max_initial_split_size. (#21320)

## Version 445
[Release Notes](https://trino.io/docs/current/release/release-445.html)

Breaking changes:
* ⚠️ Breaking change: Remove the deprecated legacy.materialized-view-grace-period
configuration property. (#21474)
* ⚠️ Breaking change: Remove the deprecated PARTITION_COLUMN and PARTITION_VALUE
arguments from the flush_metadata_cache procedure in favor of
PARTITION_COLUMNS and PARTITION_VALUES. (#21410)

## Version 446
[Release Notes](https://trino.io/docs/current/release/release-446.html)

Breaking changes:
* ⚠️ Breaking change: Enable bigquery.arrow-serialization.enabled by default. This
requires --add-opens=java.base/java.nio=ALL-UNNAMED in
jvm-config. (#21580)

## Version 447
[Release Notes](https://trino.io/docs/current/release/release-447.html)

Breaking changes:
* ⚠️ Breaking change: Require JDK 22 to run Trino, including updated JVM config.(#20980)
* ⚠️ Breaking change: Remove support for Phoenix versions 5.1.x and earlier. (#21569)
* ⚠️ Breaking change: Remove deprecated legacy type mapping and the associated
redshift.use-legacy-type-mapping configuration property. (#21855)

## Version 448
[Release Notes](https://trino.io/docs/current/release/release-448.html)

Breaking changes:
* Update Glue to V2 REST interface. The old implementation can be temporarily
restored by setting the hive.metastore configuration property to glue-v1. (#20657)

⚠️ Breaking change: The new implementation does not support and ignores the following
configuration properties: hive.metastore-refresh-interval,
hive.metastore-refresh-max-threads, hive.metastore-cache.cache-partitions,
hive.metastore-cache.cache-missing, hive.metastore-cache.cache-missing-partitions,
hive.metastore-cache.cache-missing-stats.


* ⚠️ Breaking change: The new implementation does not support and ignores the following
configuration properties: hive.metastore-refresh-interval,
hive.metastore-refresh-max-threads, hive.metastore-cache.cache-partitions,
hive.metastore-cache.cache-missing, hive.metastore-cache.cache-missing-partitions,
hive.metastore-cache.cache-missing-stats.
* Update Glue to V2 REST interface. The old implementation can be temporarily
restored by setting the hive.metastore configuration property to glue-v1. (#20657)

⚠️ Breaking change: The new implementation does not support and ignores the following
configuration properties: hive.metastore-refresh-interval,
hive.metastore-refresh-max-threads, hive.metastore-cache.cache-partitions,
hive.metastore-cache.cache-missing, hive.metastore-cache.cache-missing-partitions,
hive.metastore-cache.cache-missing-stats.


* ⚠️ Breaking change: The new implementation does not support and ignores the following
configuration properties: hive.metastore-refresh-interval,
hive.metastore-refresh-max-threads, hive.metastore-cache.cache-partitions,
hive.metastore-cache.cache-missing, hive.metastore-cache.cache-missing-partitions,
hive.metastore-cache.cache-missing-stats.
* Update Glue to V2 REST interface. The old implementation can be temporarily
restored by setting the hive.metastore configuration property to glue-v1. (#20657)

⚠️ Breaking change: The new implementation does not support and ignores the following
configuration properties: hive.metastore-refresh-interval,
hive.metastore-refresh-max-threads, hive.metastore-cache.cache-partitions,
hive.metastore-cache.cache-missing, hive.metastore-cache.cache-missing-partitions,
hive.metastore-cache.cache-missing-stats.


* ⚠️ Breaking change: The new implementation does not support and ignores the following
configuration properties: hive.metastore-refresh-interval,
hive.metastore-refresh-max-threads, hive.metastore-cache.cache-partitions,
hive.metastore-cache.cache-missing, hive.metastore-cache.cache-missing-partitions,
hive.metastore-cache.cache-missing-stats.

## Version 449
[Release Notes](https://trino.io/docs/current/release/release-449.html)

Breaking changes:
* ⚠️ Breaking change: Remove support for non-gRPC clients and the pinot.grpc.enabled
and pinot.estimated-size-in-bytes-for-non-numeric-column configuration
properties. (#22213)

## Version 450
[Release Notes](https://trino.io/docs/current/release/release-450.html)

Breaking changes:
* ⚠️ Breaking change: Improve performance of aggregations containing a DISTINCT
clause, and replace the optimizer.mark-distinct-strategy and
optimizer.optimize-mixed-distinct-aggregations configuration properties with
the new optimizer.distinct-aggregations-strategy property. (#21907)
* ⚠️ Breaking change: Automatically configure BigQuery scan parallelism, and remove the
bigquery.parallelism configuration property. (#22279)
* ⚠️ Breaking change: Add support for V2 of the Nessie REST API. Previous behavior can
be restored by setting the iceberg.nessie-catalog.client-api-version
configuration property to V1. (#22215)

