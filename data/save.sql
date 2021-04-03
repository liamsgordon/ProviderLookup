'''

CREATE TABLE public.core_provider
(
    id integer NOT NULL DEFAULT nextval('core_provider_id_seq'::regclass),
    npi character varying(10) COLLATE pg_catalog."default" NOT NULL,
    entity_code character varying(10) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    organization character varying(255) COLLATE pg_catalog."default" NOT NULL,
    postal_code character varying(50) COLLATE pg_catalog."default" NOT NULL,
    city character varying(50) COLLATE pg_catalog."default" NOT NULL,
    state character varying(40) COLLATE pg_catalog."default" NOT NULL,
    address character varying(255) COLLATE pg_catalog."default" NOT NULL,
    country character varying(255) COLLATE pg_catalog."default" NOT NULL,
    telephone_number character varying(50) COLLATE pg_catalog."default" NOT NULL,
    mail_postal_code character varying(50) COLLATE pg_catalog."default" NOT NULL,
    mail_city character varying(50) COLLATE pg_catalog."default" NOT NULL,
    mail_state character varying(40) COLLATE pg_catalog."default" NOT NULL,
    mail_address character varying(255) COLLATE pg_catalog."default" NOT NULL,
    mail_country character varying(255) COLLATE pg_catalog."default" NOT NULL,
    gender character varying(255) COLLATE pg_catalog."default" NOT NULL,
    sole_proprietor character varying(255) COLLATE pg_catalog."default" NOT NULL,
    enumeration_date character varying(255) COLLATE pg_catalog."default" NOT NULL,
    certification_date character varying(255) COLLATE pg_catalog."default" NOT NULL,
    tax_code character varying(255) COLLATE pg_catalog."default" NOT NULL,
    tax_group character varying(255) COLLATE pg_catalog."default" NOT NULL,
    tax_defintion character varying(5000) COLLATE pg_catalog."default" NOT NULL,
    tax_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT core_provider_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.core_provider
    OWNER to postgres;
-- Index: city_index

-- DROP INDEX public.city_index;

CREATE INDEX city_index
    ON public.core_provider USING btree
    (city COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: first_name_index

-- DROP INDEX public.first_name_index;

CREATE INDEX first_name_index
    ON public.core_provider USING btree
    (first_name COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: id_index

-- DROP INDEX public.id_index;

CREATE INDEX id_index
    ON public.core_provider USING btree
    (id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: last_name_index

-- DROP INDEX public.last_name_index;

CREATE INDEX last_name_index
    ON public.core_provider USING btree
    (last_name COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: name_firstlast_index

-- DROP INDEX public.name_firstlast_index;

CREATE INDEX name_firstlast_index
    ON public.core_provider USING btree
    (first_name COLLATE pg_catalog."default" ASC NULLS LAST, last_name COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: npi_index

-- DROP INDEX public.npi_index;

CREATE INDEX npi_index
    ON public.core_provider USING btree
    (npi COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: postal_index

-- DROP INDEX public.postal_index;

CREATE INDEX postal_index
    ON public.core_provider USING btree
    (postal_code COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: state_index

-- DROP INDEX public.state_index;

CREATE INDEX state_index
    ON public.core_provider USING btree
    (state COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: tax_name_index

-- DROP INDEX public.tax_name_index;

CREATE INDEX tax_name_index
    ON public.core_provider USING btree
    (tax_name COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

'''