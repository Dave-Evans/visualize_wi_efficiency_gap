/*For simplifying and building the geojson
export using
psql -d wieff -f this_file.sql -o asm.json -t -q 
*/

SELECT jsonb_build_object(
    'type',     'FeatureCollection',
    'features', jsonb_agg(feature)
)

FROM (
  SELECT jsonb_build_object(
    'type',       'Feature',
    'id',         asm,
    'geometry',   ST_AsGeoJSON(mpoly)::jsonb,
    'properties', to_jsonb(row) - 'mpoly'
  ) AS feature
  FROM (
	SELECT
		id
		, asm
		, asmdem16
		, asmrep16
		, asmdemwasted16
		, asmrepwasted16
		, asmtot16
		, asmdem14
		, asmrep14
		, asmdemwasted14
		, asmrepwasted14
		, asmtot14	
		, ST_Simplify(mpoly, 0.01) as mpoly
		FROM map_asmdistricts) row) features;
