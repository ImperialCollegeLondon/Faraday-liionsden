# Database schema

## High-level overview

For partially historic reasons, Liionsden is split into three apps:

- **BattDB** contains all the key models including `DeviceSpecification`,
  `Experiment` etc.
- **dfndb** contains models like `Compound`, `Component`, `QuantityUnit` etc.,
  which are [related to the DFN
  model](https://github.com/ndrewwang/dfndb-django) parameters.
- **common** contains mostly abstract models with common fields that models in
  the other apps inherit from. This helps to keep the code
  [DRY](https://www.digitalocean.com/community/tutorials/what-is-dry-development).

The important model relationships can be best understood by considering the
intended workflow for adding data to the database:

1. **Define a device specification:** This involves creating a new
   `battDB.DeviceSpecification` object, and optionally related `dfndb.Component`
   objects that make up the device and `dfndb.Parameter` objects that define its
   capacity, dimensions etc.
2. **Add a batch of those devices:** A `battDB.batch` is related to one
   `battDB.DeviceSpecification` and represents a physical collection of devices.
3. **Create an experiment using those devices:**
    - A new `battDB.Experiment` object represents an experiment in which some
      devices from a batch are measured.
    - New `battDB.ExperimentDevice` objects are created to associate devices
      with the experiment.
    - Each `battDB.ExperimentDevice` objects is associated with a `battDB.Batch`
      and has a `batch_sequence` integer field. In the
      `ExperimentDevice.clean()` method, an associated `battDB.Device` object is
      created.
    - **The above means that `battDB.Device` objects only exist once a device is
      registered as being used in an experiment.**
4. **Associate data with that experiment:**
    - One or more `battDB.ExperimentDataFile` objects can then be associated
      with a `battDB.Experiment`.
    - The `battDB.ExperimentDataFile` is associated with a `battDB.Device`,
      which is why these are created in advance when a `battDB.Experiment` is
      made.
    - The `battDB.ExperimentDataFile` is associated with parsed data (`ts_data`
      field), `battDB.Equipment` and raw data files.

## Tips for determining model relationships

- **Several models are itermediate:** For many-to-many (M2M) relationships in
  Django an intermediary is often used, which itself has ForeignKey
  relationships to each of the two other models. For example, the
  `DeviceComponent` handles the M2M relationship between `DeviceSpecification`
  and `Component`:

    ```python
    class DeviceSpecification(cm.BaseModelMandatoryName, cm.HasMPTT):

        components = models.ManyToManyField(dfn.Component, through="DeviceComponent")

    ...

    class DeviceComponent(cm.HasName):

        spec = models.ForeignKey(DeviceSpecification, on_delete=models.CASCADE)
        component = models.ForeignKey(dfn.Component, on_delete=models.CASCADE)
    ```

- **Produce a graph of relationships:** see below.

## Complete visualisation of database schema

To visualise all the database relationships follow the [instructions on the
django-extension docs for producing graph
models](https://django-extensions.readthedocs.io/en/latest/graph_models.html).
We don't include a complete visualisation here as it is too complicated to be
helpful. Any graph view you produce will need to be customised to only include
certain apps, models and relationships depending on what you are trying to show.
We also don't include `pygraphviz` explicity in dev-docs because depending on
your local setup, you may have to separately configure `graphviz` itself (see
[example for Homebrew installation on
Mac](https://dev.to/javanibble/how-to-install-graphviz-on-macos-using-homebrew-3ig3)).
