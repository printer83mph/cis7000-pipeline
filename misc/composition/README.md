# Composition!!!

Goal: Manually create a scene that uses at least 4 different arcs and uses the assets from our last assignment

**4 arcs used: sublayers, payload, references, variants**

1. Sublayers: our root `scene.usda` has two sublayers, one being `scene_set.usda` and the other `scene_layer.usda`
2. Payload: within `scene_set.usda`, there is a "high poly" chef character behind a payload
3. References: `scene_set.usda` includes references to each original asset
4. Variants: assets (`example_asset.usda`) have an `lodVariant` set which specifies `low`, `medium`, or `high`