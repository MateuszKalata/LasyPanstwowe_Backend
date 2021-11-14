DROP TABLE IF EXISTS "forest_areas";
DROP SEQUENCE IF EXISTS forest_areas_id_seq;
CREATE SEQUENCE forest_areas_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."forest_areas" (
    "id" integer DEFAULT nextval('forest_areas_id_seq') NOT NULL,
    "forestry_id" integer,
    "name" character varying(200),
    "surface" character varying(200),
    CONSTRAINT "forest_areas_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "forestation_types";
DROP SEQUENCE IF EXISTS forestation_types_id_seq;
CREATE SEQUENCE forestation_types_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."forestation_types" (
    "id" integer DEFAULT nextval('forestation_types_id_seq') NOT NULL,
    "forest_area_id" integer,
    "name" character varying(200),
    "surface" character varying(200),
    CONSTRAINT "forestation_types_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "forestries";
DROP SEQUENCE IF EXISTS forestries_id_seq;
CREATE SEQUENCE forestries_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."forestries" (
    "id" integer DEFAULT nextval('forestries_id_seq') NOT NULL,
    "name" character varying(200),
    "surface" character varying(200),
    CONSTRAINT "forestries_pkey" PRIMARY KEY ("id")
) WITH (oids = false);