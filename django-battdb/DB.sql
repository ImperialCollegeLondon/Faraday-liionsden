--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0 (Debian 13.0-2)
-- Dumped by pg_dump version 13.0 (Debian 13.0-2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO towen;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO towen;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO towen;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO towen;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO towen;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO towen;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO towen;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO towen;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO towen;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO towen;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO towen;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO towen;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO towen;

--
-- Name: battDB_cellconfig; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_cellconfig" (
    id integer NOT NULL,
    attributes jsonb NOT NULL,
    num_cells integer NOT NULL,
    status smallint NOT NULL,
    user_owner_id integer,
    name character varying(128),
    notes text,
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT "battDB_cellconfig_num_cells_check" CHECK ((num_cells >= 0)),
    CONSTRAINT "battDB_cellconfig_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_cellconfig" OWNER TO towen;

--
-- Name: battDB_cellconfig_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_cellconfig_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_cellconfig_id_seq" OWNER TO towen;

--
-- Name: battDB_cellconfig_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_cellconfig_id_seq" OWNED BY public."battDB_cellconfig".id;


--
-- Name: battDB_datarange; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_datarange" (
    id integer NOT NULL,
    label character varying(32),
    protocol_step integer NOT NULL,
    step_action character varying(8),
    ts_headers character varying(32)[],
    ts_data double precision[],
    "dataFile_id" integer,
    file_offset integer NOT NULL,
    attributes jsonb NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    user_owner_id integer,
    notes text,
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT "battDB_datarange_file_offset_check" CHECK ((file_offset >= 0)),
    CONSTRAINT "battDB_datarange_protocol_step_check" CHECK ((protocol_step >= 0)),
    CONSTRAINT "battDB_datarange_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_datarange" OWNER TO towen;

--
-- Name: battDB_datarange_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_datarange_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_datarange_id_seq" OWNER TO towen;

--
-- Name: battDB_datarange_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_datarange_id_seq" OWNED BY public."battDB_datarange".id;


--
-- Name: battDB_devicebatch; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_devicebatch" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    device_type_id integer,
    manufacturer_id integer,
    user_owner_id integer,
    manufactured_on date,
    CONSTRAINT "battDB_devicebatch_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_devicebatch" OWNER TO towen;

--
-- Name: battDB_devicebatch_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_devicebatch_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_devicebatch_id_seq" OWNER TO towen;

--
-- Name: battDB_devicebatch_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_devicebatch_id_seq" OWNED BY public."battDB_devicebatch".id;


--
-- Name: battDB_deviceconfig; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_deviceconfig" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    user_owner_id integer,
    CONSTRAINT "battDB_deviceconfig_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_deviceconfig" OWNER TO towen;

--
-- Name: battDB_deviceconfig_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_deviceconfig_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_deviceconfig_id_seq" OWNER TO towen;

--
-- Name: battDB_deviceconfig_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_deviceconfig_id_seq" OWNED BY public."battDB_deviceconfig".id;


--
-- Name: battDB_deviceconfignode; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_deviceconfignode" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    "deviceConfig_id" integer NOT NULL,
    "deviceType_id" integer NOT NULL,
    user_owner_id integer,
    CONSTRAINT "battDB_deviceconfignode_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_deviceconfignode" OWNER TO towen;

--
-- Name: battDB_deviceconfignode_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_deviceconfignode_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_deviceconfignode_id_seq" OWNER TO towen;

--
-- Name: battDB_deviceconfignode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_deviceconfignode_id_seq" OWNED BY public."battDB_deviceconfignode".id;


--
-- Name: battDB_devicetype; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_devicetype" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    type smallint NOT NULL,
    user_owner_id integer,
    CONSTRAINT "battDB_devicetype_status_check" CHECK ((status >= 0)),
    CONSTRAINT "battDB_devicetype_type_check" CHECK ((type >= 0))
);


ALTER TABLE public."battDB_devicetype" OWNER TO towen;

--
-- Name: battDB_devicetype_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_devicetype_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_devicetype_id_seq" OWNER TO towen;

--
-- Name: battDB_devicetype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_devicetype_id_seq" OWNED BY public."battDB_devicetype".id;


--
-- Name: battDB_equipment; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_equipment" (
    id integer NOT NULL,
    attributes jsonb NOT NULL,
    "serialNo" character varying(64) NOT NULL,
    type_id integer,
    status smallint NOT NULL,
    user_owner_id integer,
    name character varying(128),
    notes text,
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT "battDB_equipment_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_equipment" OWNER TO towen;

--
-- Name: battDB_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_equipment_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_equipment_id_seq" OWNER TO towen;

--
-- Name: battDB_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_equipment_id_seq" OWNED BY public."battDB_equipment".id;


--
-- Name: battDB_equipmenttype; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_equipmenttype" (
    id integer NOT NULL,
    attributes jsonb NOT NULL,
    status smallint NOT NULL,
    user_owner_id integer,
    name character varying(128),
    notes text,
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT "battDB_equipmenttype_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_equipmenttype" OWNER TO towen;

--
-- Name: battDB_equipmenttype_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_equipmenttype_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_equipmenttype_id_seq" OWNER TO towen;

--
-- Name: battDB_equipmenttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_equipmenttype_id_seq" OWNED BY public."battDB_equipmenttype".id;


--
-- Name: battDB_experiment; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_experiment" (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    date date NOT NULL,
    user_owner_id integer,
    status character varying(16) NOT NULL,
    protocol_id integer,
    "cellConfig_id" integer,
    attributes jsonb NOT NULL,
    notes text,
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL
);


ALTER TABLE public."battDB_experiment" OWNER TO towen;

--
-- Name: battDB_experiment_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_experiment_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_experiment_id_seq" OWNER TO towen;

--
-- Name: battDB_experiment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_experiment_id_seq" OWNED BY public."battDB_experiment".id;


--
-- Name: battDB_experimentdatafile; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_experimentdatafile" (
    id integer NOT NULL,
    raw_data_file_id integer NOT NULL,
    experiment_id integer,
    machine_id integer,
    status smallint NOT NULL,
    user_owner_id integer,
    attributes jsonb NOT NULL,
    name character varying(128),
    notes text,
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT "battDB_experimentdatafile_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_experimentdatafile" OWNER TO towen;

--
-- Name: battDB_experimentdatafile_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_experimentdatafile_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_experimentdatafile_id_seq" OWNER TO towen;

--
-- Name: battDB_experimentdatafile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_experimentdatafile_id_seq" OWNED BY public."battDB_experimentdatafile".id;


--
-- Name: battDB_module; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_module" (
    device_ptr_id integer NOT NULL
);


ALTER TABLE public."battDB_module" OWNER TO towen;

--
-- Name: battDB_pack; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_pack" (
    device_ptr_id integer NOT NULL
);


ALTER TABLE public."battDB_pack" OWNER TO towen;

--
-- Name: battDB_rawdatafile; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_rawdatafile" (
    id integer NOT NULL,
    status smallint NOT NULL,
    attributes jsonb NOT NULL,
    raw_data_file character varying(100),
    user_owner_id integer,
    name character varying(128),
    notes text,
    file_hash character varying(64) NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT "battDB_rawdatafile_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_rawdatafile" OWNER TO towen;

--
-- Name: battDB_rawdatafile_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_rawdatafile_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_rawdatafile_id_seq" OWNER TO towen;

--
-- Name: battDB_rawdatafile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_rawdatafile_id_seq" OWNED BY public."battDB_rawdatafile".id;


--
-- Name: common_basemodelwithslug; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.common_basemodelwithslug (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(50) NOT NULL,
    user_owner_id integer,
    CONSTRAINT common_basemodelwithslug_status_check CHECK ((status >= 0))
);


ALTER TABLE public.common_basemodelwithslug OWNER TO towen;

--
-- Name: common_basemodelwithslug_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.common_basemodelwithslug_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.common_basemodelwithslug_id_seq OWNER TO towen;

--
-- Name: common_basemodelwithslug_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.common_basemodelwithslug_id_seq OWNED BY public.common_basemodelwithslug.id;


--
-- Name: common_org; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.common_org (
    id integer NOT NULL,
    website character varying(200),
    is_mfg_cells boolean NOT NULL,
    is_mfg_equip boolean NOT NULL,
    is_publisher boolean NOT NULL,
    is_research boolean NOT NULL,
    manager_id integer,
    name character varying(128) NOT NULL
);


ALTER TABLE public.common_org OWNER TO towen;

--
-- Name: common_org_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.common_org_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.common_org_id_seq OWNER TO towen;

--
-- Name: common_org_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.common_org_id_seq OWNED BY public.common_org.id;


--
-- Name: common_paper; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.common_paper (
    id integer NOT NULL,
    "DOI" character varying(128),
    year integer NOT NULL,
    title character varying(300) NOT NULL,
    url character varying(200),
    publisher_id integer,
    attributes jsonb NOT NULL,
    status smallint NOT NULL,
    user_owner_id integer,
    notes text,
    "PDF" character varying(100),
    modified_on timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    slug character varying(50) NOT NULL,
    CONSTRAINT common_paper_status_check CHECK ((status >= 0))
);


ALTER TABLE public.common_paper OWNER TO towen;

--
-- Name: common_paper_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.common_paper_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.common_paper_id_seq OWNER TO towen;

--
-- Name: common_paper_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.common_paper_id_seq OWNED BY public.common_paper.id;


--
-- Name: common_paperauthor; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.common_paperauthor (
    id integer NOT NULL,
    is_principal boolean NOT NULL,
    author_id integer NOT NULL,
    paper_id integer NOT NULL
);


ALTER TABLE public.common_paperauthor OWNER TO towen;

--
-- Name: common_paperauthor_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.common_paperauthor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.common_paperauthor_id_seq OWNER TO towen;

--
-- Name: common_paperauthor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.common_paperauthor_id_seq OWNED BY public.common_paperauthor.id;


--
-- Name: common_person; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.common_person (
    id integer NOT NULL,
    org_id integer,
    user_id integer,
    "longName" character varying(128) NOT NULL,
    "shortName" character varying(128) NOT NULL
);


ALTER TABLE public.common_person OWNER TO towen;

--
-- Name: common_person_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.common_person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.common_person_id_seq OWNER TO towen;

--
-- Name: common_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.common_person_id_seq OWNED BY public.common_person.id;


--
-- Name: dfndb_compositionpart; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_compositionpart (
    id integer NOT NULL,
    amount smallint NOT NULL,
    compound_id integer NOT NULL,
    material_id integer NOT NULL,
    CONSTRAINT dfndb_compositionpart_amount_28a98350_check CHECK ((amount >= 0))
);


ALTER TABLE public.dfndb_compositionpart OWNER TO towen;

--
-- Name: dfndb_compositionpart_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_compositionpart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_compositionpart_id_seq OWNER TO towen;

--
-- Name: dfndb_compositionpart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_compositionpart_id_seq OWNED BY public.dfndb_compositionpart.id;


--
-- Name: dfndb_compound; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_compound (
    id integer NOT NULL,
    formula character varying(20) NOT NULL,
    name character varying(100) NOT NULL,
    mass integer NOT NULL,
    CONSTRAINT dfndb_compound_mass_check CHECK ((mass >= 0))
);


ALTER TABLE public.dfndb_compound OWNER TO towen;

--
-- Name: dfndb_compound_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_compound_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_compound_id_seq OWNER TO towen;

--
-- Name: dfndb_compound_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_compound_id_seq OWNED BY public.dfndb_compound.id;


--
-- Name: dfndb_data; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_data (
    id integer NOT NULL,
    paper_id integer,
    user_owner_id integer,
    attributes jsonb NOT NULL,
    status smallint NOT NULL,
    name character varying(128),
    notes text,
    modified_on date NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT dfndb_data_status_check CHECK ((status >= 0))
);


ALTER TABLE public.dfndb_data OWNER TO towen;

--
-- Name: dfndb_data_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_data_id_seq OWNER TO towen;

--
-- Name: dfndb_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_data_id_seq OWNED BY public.dfndb_data.id;


--
-- Name: dfndb_dataparameter; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_dataparameter (
    id integer NOT NULL,
    data_id integer NOT NULL,
    parameter_id integer NOT NULL,
    material_id integer,
    type smallint NOT NULL,
    value jsonb,
    CONSTRAINT dfndb_dataparameter_type_check CHECK ((type >= 0))
);


ALTER TABLE public.dfndb_dataparameter OWNER TO towen;

--
-- Name: dfndb_dataparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_dataparameter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_dataparameter_id_seq OWNER TO towen;

--
-- Name: dfndb_dataparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_dataparameter_id_seq OWNED BY public.dfndb_dataparameter.id;


--
-- Name: dfndb_material; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_material (
    id integer NOT NULL,
    polymer integer NOT NULL,
    user_owner_id integer,
    type smallint NOT NULL,
    attributes jsonb NOT NULL,
    status smallint NOT NULL,
    name character varying(128),
    notes text,
    modified_on date NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT dfndb_material_polymer_cda0da24_check CHECK ((polymer >= 0)),
    CONSTRAINT dfndb_material_status_check CHECK ((status >= 0)),
    CONSTRAINT dfndb_material_type_19d56e15_check CHECK ((type >= 0))
);


ALTER TABLE public.dfndb_material OWNER TO towen;

--
-- Name: dfndb_material_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_material_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_material_id_seq OWNER TO towen;

--
-- Name: dfndb_material_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_material_id_seq OWNED BY public.dfndb_material.id;


--
-- Name: dfndb_method; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_method (
    id integer NOT NULL,
    type integer NOT NULL,
    description text NOT NULL,
    user_owner_id integer,
    attributes jsonb NOT NULL,
    status smallint NOT NULL,
    name character varying(128),
    notes text,
    modified_on date NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT dfndb_method_status_check CHECK ((status >= 0))
);


ALTER TABLE public.dfndb_method OWNER TO towen;

--
-- Name: dfndb_method_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_method_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_method_id_seq OWNER TO towen;

--
-- Name: dfndb_method_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_method_id_seq OWNED BY public.dfndb_method.id;


--
-- Name: dfndb_parameter; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_parameter (
    id integer NOT NULL,
    symbol character varying(40) NOT NULL,
    notes text,
    unit_id integer,
    user_owner_id integer,
    attributes jsonb NOT NULL,
    status smallint NOT NULL,
    name character varying(128),
    modified_on date NOT NULL,
    created_on timestamp with time zone NOT NULL,
    CONSTRAINT dfndb_parameter_status_check CHECK ((status >= 0))
);


ALTER TABLE public.dfndb_parameter OWNER TO towen;

--
-- Name: dfndb_parameter_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_parameter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_parameter_id_seq OWNER TO towen;

--
-- Name: dfndb_parameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_parameter_id_seq OWNED BY public.dfndb_parameter.id;


--
-- Name: dfndb_quantityunit; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.dfndb_quantityunit (
    id integer NOT NULL,
    "quantityName" character varying(100) NOT NULL,
    "quantitySymbol" character varying(40) NOT NULL,
    "unitName" character varying(40) NOT NULL,
    "unitSymbol" character varying(40) NOT NULL,
    "is_SI_unit" boolean NOT NULL,
    related_scale double precision,
    related_unit_id integer
);


ALTER TABLE public.dfndb_quantityunit OWNER TO towen;

--
-- Name: dfndb_quantityunit_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.dfndb_quantityunit_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfndb_quantityunit_id_seq OWNER TO towen;

--
-- Name: dfndb_quantityunit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.dfndb_quantityunit_id_seq OWNED BY public.dfndb_quantityunit.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO towen;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO towen;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO towen;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO towen;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO towen;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO towen;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO towen;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: battDB_cellconfig id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_cellconfig" ALTER COLUMN id SET DEFAULT nextval('public."battDB_cellconfig_id_seq"'::regclass);


--
-- Name: battDB_datarange id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datarange" ALTER COLUMN id SET DEFAULT nextval('public."battDB_datarange_id_seq"'::regclass);


--
-- Name: battDB_devicebatch id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch" ALTER COLUMN id SET DEFAULT nextval('public."battDB_devicebatch_id_seq"'::regclass);


--
-- Name: battDB_deviceconfig id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfig" ALTER COLUMN id SET DEFAULT nextval('public."battDB_deviceconfig_id_seq"'::regclass);


--
-- Name: battDB_deviceconfignode id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfignode" ALTER COLUMN id SET DEFAULT nextval('public."battDB_deviceconfignode_id_seq"'::regclass);


--
-- Name: battDB_devicetype id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicetype" ALTER COLUMN id SET DEFAULT nextval('public."battDB_devicetype_id_seq"'::regclass);


--
-- Name: battDB_equipment id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment" ALTER COLUMN id SET DEFAULT nextval('public."battDB_equipment_id_seq"'::regclass);


--
-- Name: battDB_equipmenttype id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipmenttype" ALTER COLUMN id SET DEFAULT nextval('public."battDB_equipmenttype_id_seq"'::regclass);


--
-- Name: battDB_experiment id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experiment_id_seq"'::regclass);


--
-- Name: battDB_experimentdatafile id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experimentdatafile_id_seq"'::regclass);


--
-- Name: battDB_rawdatafile id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_rawdatafile" ALTER COLUMN id SET DEFAULT nextval('public."battDB_rawdatafile_id_seq"'::regclass);


--
-- Name: common_basemodelwithslug id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_basemodelwithslug ALTER COLUMN id SET DEFAULT nextval('public.common_basemodelwithslug_id_seq'::regclass);


--
-- Name: common_org id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_org ALTER COLUMN id SET DEFAULT nextval('public.common_org_id_seq'::regclass);


--
-- Name: common_paper id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paper ALTER COLUMN id SET DEFAULT nextval('public.common_paper_id_seq'::regclass);


--
-- Name: common_paperauthor id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paperauthor ALTER COLUMN id SET DEFAULT nextval('public.common_paperauthor_id_seq'::regclass);


--
-- Name: common_person id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person ALTER COLUMN id SET DEFAULT nextval('public.common_person_id_seq'::regclass);


--
-- Name: dfndb_compositionpart id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compositionpart ALTER COLUMN id SET DEFAULT nextval('public.dfndb_compositionpart_id_seq'::regclass);


--
-- Name: dfndb_compound id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compound ALTER COLUMN id SET DEFAULT nextval('public.dfndb_compound_id_seq'::regclass);


--
-- Name: dfndb_data id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_data ALTER COLUMN id SET DEFAULT nextval('public.dfndb_data_id_seq'::regclass);


--
-- Name: dfndb_dataparameter id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_dataparameter ALTER COLUMN id SET DEFAULT nextval('public.dfndb_dataparameter_id_seq'::regclass);


--
-- Name: dfndb_material id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_material ALTER COLUMN id SET DEFAULT nextval('public.dfndb_material_id_seq'::regclass);


--
-- Name: dfndb_method id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_method ALTER COLUMN id SET DEFAULT nextval('public.dfndb_method_id_seq'::regclass);


--
-- Name: dfndb_parameter id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_parameter ALTER COLUMN id SET DEFAULT nextval('public.dfndb_parameter_id_seq'::regclass);


--
-- Name: dfndb_quantityunit id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_quantityunit ALTER COLUMN id SET DEFAULT nextval('public.dfndb_quantityunit_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_group (id, name) FROM stdin;
1	Administrators
2	Experimenters
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
26	1	26
27	1	27
28	1	28
29	1	29
30	1	30
31	1	31
32	1	32
33	1	33
34	1	34
35	1	35
36	1	36
37	1	37
38	1	38
39	1	39
40	1	40
41	1	41
42	1	42
43	1	43
44	1	44
45	1	45
46	1	46
47	1	47
48	1	48
49	1	49
50	1	50
51	1	51
52	1	52
53	1	53
54	1	54
55	1	55
56	1	56
57	1	57
58	1	58
59	1	59
60	1	60
61	1	61
62	1	62
63	1	63
64	1	64
65	1	65
66	1	66
67	1	67
68	1	68
69	2	1
70	2	2
71	2	3
72	2	4
73	2	5
74	2	6
75	2	7
76	2	8
77	2	9
78	2	10
79	2	11
80	2	12
81	2	13
82	2	14
83	2	15
84	2	16
85	2	17
86	2	18
87	2	19
88	2	20
89	2	21
90	2	22
91	2	23
92	2	24
93	2	25
94	2	26
95	2	27
96	2	28
97	2	29
98	2	30
99	2	31
100	2	32
101	2	33
102	2	34
103	2	35
104	2	36
105	2	61
106	2	62
107	2	63
108	2	64
109	2	65
110	2	66
111	2	67
112	2	68
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add cell	1	add_cell
2	Can change cell	1	change_cell
3	Can delete cell	1	delete_cell
4	Can view cell	1	view_cell
5	Can add cell separator	2	add_cellseparator
6	Can change cell separator	2	change_cellseparator
7	Can delete cell separator	2	delete_cellseparator
8	Can view cell separator	2	view_cellseparator
9	Can add equipment	3	add_equipment
10	Can change equipment	3	change_equipment
11	Can delete equipment	3	delete_equipment
12	Can view equipment	3	view_equipment
13	Can add manufacturer	4	add_manufacturer
14	Can change manufacturer	4	change_manufacturer
15	Can delete manufacturer	4	delete_manufacturer
16	Can view manufacturer	4	view_manufacturer
17	Can add signal type	5	add_signaltype
18	Can change signal type	5	change_signaltype
19	Can delete signal type	5	delete_signaltype
20	Can view signal type	5	view_signaltype
21	Can add test protocol	6	add_testprotocol
22	Can change test protocol	6	change_testprotocol
23	Can delete test protocol	6	delete_testprotocol
24	Can view test protocol	6	view_testprotocol
25	Can add experimental apparatus	7	add_experimentalapparatus
26	Can change experimental apparatus	7	change_experimentalapparatus
27	Can delete experimental apparatus	7	delete_experimentalapparatus
28	Can view experimental apparatus	7	view_experimentalapparatus
29	Can add experiment	8	add_experiment
30	Can change experiment	8	change_experiment
31	Can delete experiment	8	delete_experiment
32	Can view experiment	8	view_experiment
33	Can add cell batch	9	add_cellbatch
34	Can change cell batch	9	change_cellbatch
35	Can delete cell batch	9	delete_cellbatch
36	Can view cell batch	9	view_cellbatch
37	Can add permission	10	add_permission
38	Can change permission	10	change_permission
39	Can delete permission	10	delete_permission
40	Can view permission	10	view_permission
41	Can add group	11	add_group
42	Can change group	11	change_group
43	Can delete group	11	delete_group
44	Can view group	11	view_group
45	Can add user	12	add_user
46	Can change user	12	change_user
47	Can delete user	12	delete_user
48	Can view user	12	view_user
49	Can add content type	13	add_contenttype
50	Can change content type	13	change_contenttype
51	Can delete content type	13	delete_contenttype
52	Can view content type	13	view_contenttype
53	Can add log entry	14	add_logentry
54	Can change log entry	14	change_logentry
55	Can delete log entry	14	delete_logentry
56	Can view log entry	14	view_logentry
57	Can add session	15	add_session
58	Can change session	15	change_session
59	Can delete session	15	delete_session
60	Can view session	15	view_session
61	Can add equipment type	16	add_equipmenttype
62	Can change equipment type	16	change_equipmenttype
63	Can delete equipment type	16	delete_equipmenttype
64	Can view equipment type	16	view_equipmenttype
65	Can add cell config	17	add_cellconfig
66	Can change cell config	17	change_cellconfig
67	Can delete cell config	17	delete_cellconfig
68	Can view cell config	17	view_cellconfig
69	Can add experiment result	18	add_experimentresult
70	Can change experiment result	18	change_experimentresult
71	Can delete experiment result	18	delete_experimentresult
72	Can view experiment result	18	view_experimentresult
73	Can add experiment data	19	add_experimentdata
74	Can change experiment data	19	change_experimentdata
75	Can delete experiment data	19	delete_experimentdata
76	Can view experiment data	19	view_experimentdata
77	Can add e c_ cycle	20	add_ec_cycle
78	Can change e c_ cycle	20	change_ec_cycle
79	Can delete e c_ cycle	20	delete_ec_cycle
80	Can view e c_ cycle	20	view_ec_cycle
81	Can add cell type	21	add_celltype
82	Can change cell type	21	change_celltype
83	Can delete cell type	21	delete_celltype
84	Can view cell type	21	view_celltype
85	Can add data range	22	add_datarange
86	Can change data range	22	change_datarange
87	Can delete data range	22	delete_datarange
88	Can view data range	22	view_datarange
89	Can add experiment data file	23	add_experimentdatafile
90	Can change experiment data file	23	change_experimentdatafile
91	Can delete experiment data file	23	delete_experimentdatafile
92	Can view experiment data file	23	view_experimentdatafile
93	Can add dash app	24	add_dashapp
94	Can change dash app	24	change_dashapp
95	Can delete dash app	24	delete_dashapp
96	Can view dash app	24	view_dashapp
97	Can add stateless app	25	add_statelessapp
98	Can change stateless app	25	change_statelessapp
99	Can delete stateless app	25	delete_statelessapp
100	Can view stateless app	25	view_statelessapp
101	Can add paper	26	add_paper
102	Can change paper	26	change_paper
103	Can delete paper	26	delete_paper
104	Can view paper	26	view_paper
105	Can add composition part	27	add_compositionpart
106	Can change composition part	27	change_compositionpart
107	Can delete composition part	27	delete_compositionpart
108	Can view composition part	27	view_compositionpart
109	Can add compound	28	add_compound
110	Can change compound	28	change_compound
111	Can delete compound	28	delete_compound
112	Can view compound	28	view_compound
113	Can add material	29	add_material
114	Can change material	29	change_material
115	Can delete material	29	delete_material
116	Can view material	29	view_material
117	Can add method	30	add_method
118	Can change method	30	change_method
119	Can delete method	30	delete_method
120	Can view method	30	view_method
121	Can add quantity unit	31	add_quantityunit
122	Can change quantity unit	31	change_quantityunit
123	Can delete quantity unit	31	delete_quantityunit
124	Can view quantity unit	31	view_quantityunit
125	Can add parameter	32	add_parameter
126	Can change parameter	32	change_parameter
127	Can delete parameter	32	delete_parameter
128	Can view parameter	32	view_parameter
129	Can add data	33	add_data
130	Can change data	33	change_data
131	Can delete data	33	delete_data
132	Can view data	33	view_data
133	Can add org	34	add_org
134	Can change org	34	change_org
135	Can delete org	34	delete_org
136	Can view org	34	view_org
137	Can add paper	35	add_paper
138	Can change paper	35	change_paper
139	Can delete paper	35	delete_paper
140	Can view paper	35	view_paper
141	Can add person	36	add_person
142	Can change person	36	change_person
143	Can delete person	36	delete_person
144	Can view person	36	view_person
145	Can add device type	37	add_devicetype
146	Can change device type	37	change_devicetype
147	Can delete device type	37	delete_devicetype
148	Can view device type	37	view_devicetype
149	Can add device batch	38	add_devicebatch
150	Can change device batch	38	change_devicebatch
151	Can delete device batch	38	delete_devicebatch
152	Can view device batch	38	view_devicebatch
153	Can add device	39	add_device
154	Can change device	39	change_device
155	Can delete device	39	delete_device
156	Can view device	39	view_device
157	Can add raw data file	40	add_rawdatafile
158	Can change raw data file	40	change_rawdatafile
159	Can delete raw data file	40	delete_rawdatafile
160	Can view raw data file	40	view_rawdatafile
161	Can add apparatus equipment	41	add_apparatusequipment
162	Can change apparatus equipment	41	change_apparatusequipment
163	Can delete apparatus equipment	41	delete_apparatusequipment
164	Can view apparatus equipment	41	view_apparatusequipment
165	Can add device type	42	add_devicetype
166	Can change device type	42	change_devicetype
167	Can delete device type	42	delete_devicetype
168	Can view device type	42	view_devicetype
169	Can add device	43	add_device
170	Can change device	43	change_device
171	Can delete device	43	delete_device
172	Can view device	43	view_device
173	Can add batch	44	add_batch
174	Can change batch	44	change_batch
175	Can delete batch	44	delete_batch
176	Can view batch	44	view_batch
177	Can add Token	45	add_token
178	Can change Token	45	change_token
179	Can delete Token	45	delete_token
180	Can view Token	45	view_token
181	Can add token	46	add_tokenproxy
182	Can change token	46	change_tokenproxy
183	Can delete token	46	delete_tokenproxy
184	Can view token	46	view_tokenproxy
185	Can add batch	47	add_batch
186	Can change batch	47	change_batch
187	Can delete batch	47	delete_batch
188	Can view batch	47	view_batch
189	Can add data parameter	48	add_dataparameter
190	Can change data parameter	48	change_dataparameter
191	Can delete data parameter	48	delete_dataparameter
192	Can view data parameter	48	view_dataparameter
193	Can add paper author	49	add_paperauthor
194	Can change paper author	49	change_paperauthor
195	Can delete paper author	49	delete_paperauthor
196	Can view paper author	49	view_paperauthor
197	Can add device config node	50	add_deviceconfignode
198	Can change device config node	50	change_deviceconfignode
199	Can delete device config node	50	delete_deviceconfignode
200	Can view device config node	50	view_deviceconfignode
201	Can add device config	51	add_deviceconfig
202	Can change device config	51	change_deviceconfig
203	Can delete device config	51	delete_deviceconfig
204	Can view device config	51	view_deviceconfig
205	Can add base model with slug	52	add_basemodelwithslug
206	Can change base model with slug	52	change_basemodelwithslug
207	Can delete base model with slug	52	delete_basemodelwithslug
208	Can view base model with slug	52	view_basemodelwithslug
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$150000$xjdfdhTwRhJ2$UXRtByrTwyL9b+c/+/4ttwBrsYYx4Z3gXbi7n7MqAyo=	\N	t	jacql	Jacqueline	Edge	j.edge@imperial.ac.uk	t	t	2020-08-11 11:11:31+01
3	pbkdf2_sha256$150000$EfLnuKoVFTo5$eI9zlUW09YuBiHiPdlpYqbf8cFyvRvTISVec8IqZaUw=	2020-08-13 10:56:28+01	t	binbin	Binbin	Chen		t	t	2020-08-13 09:53:36+01
7	pbkdf2_sha256$216000$Vt9WFAxpjSyE$nW6zcHd0uYfDqElZJ+RkFpcN3t9RDAPKyWGARyQdUw4=	2020-10-08 13:36:25.920895+01	f	test	Test	User		t	t	2020-10-08 13:33:36+01
1	pbkdf2_sha256$216000$OafoLVPyzITM$orFVUO5QzVoBneWLEpu4jxz+Ucrc+DqclzTFOsJcvH4=	2020-10-17 21:50:44.251782+01	t	tom	Tom	Owen	tom.owen@zepler.net	t	t	2020-08-04 19:08:06+01
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
1	3	2
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
1	2	1
2	2	2
3	2	3
4	2	4
5	2	5
6	2	6
7	2	7
8	2	8
9	2	9
10	2	10
11	2	11
12	2	12
13	2	13
14	2	14
15	2	15
16	2	16
17	2	17
18	2	18
19	2	19
20	2	20
21	2	21
22	2	22
23	2	23
24	2	24
25	2	25
26	2	26
27	2	27
28	2	28
29	2	29
30	2	30
31	2	31
32	2	32
33	2	33
34	2	34
35	2	35
36	2	36
37	2	37
38	2	38
39	2	39
40	2	40
41	2	41
42	2	42
43	2	43
44	2	44
45	2	45
46	2	46
47	2	47
48	2	48
49	2	49
50	2	50
51	2	51
52	2	52
53	2	53
54	2	54
55	2	55
56	2	56
57	2	57
58	2	58
59	2	59
60	2	60
61	2	61
62	2	62
63	2	63
64	2	64
65	2	65
66	2	66
67	2	67
68	2	68
69	7	128
70	7	4
71	7	132
72	7	8
73	7	136
74	7	12
75	7	140
76	7	16
77	7	144
78	7	20
79	7	24
80	7	28
81	7	32
82	7	36
83	7	40
84	7	44
85	7	48
86	7	52
87	7	56
88	7	60
89	7	64
90	7	68
91	7	72
92	7	76
93	7	80
94	7	84
95	7	88
96	7	92
97	7	96
98	7	100
99	7	104
100	7	108
101	7	112
102	7	116
103	7	120
104	7	124
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
52f1021a6e32e4202acab1c5c19f0067cc1ce38a	2020-10-14 15:46:13.411002+01	1
\.


--
-- Data for Name: battDB_cellconfig; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_cellconfig" (id, attributes, num_cells, status, user_owner_id, name, notes, modified_on, created_on) FROM stdin;
1	{}	1	20	\N	\N	\N	2020-10-15 18:13:05.465474+01	2020-10-15 18:18:04.803982+01
\.


--
-- Data for Name: battDB_datarange; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_datarange" (id, label, protocol_step, step_action, ts_headers, ts_data, "dataFile_id", file_offset, attributes, name, status, user_owner_id, notes, modified_on, created_on) FROM stdin;
1	charging	1	chg	{}	{{1},{2},{3},{4},{5},{6},{7},{8}}	\N	0	{}	\N	10	\N	\N	2020-10-15 18:13:05.539662+01	2020-10-15 18:18:04.843857+01
\.


--
-- Data for Name: battDB_devicebatch; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_devicebatch" (id, name, status, created_on, modified_on, attributes, notes, device_type_id, manufacturer_id, user_owner_id, manufactured_on) FROM stdin;
\.


--
-- Data for Name: battDB_deviceconfig; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_deviceconfig" (id, name, status, created_on, modified_on, attributes, notes, user_owner_id) FROM stdin;
\.


--
-- Data for Name: battDB_deviceconfignode; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_deviceconfignode" (id, name, status, created_on, modified_on, attributes, notes, "deviceConfig_id", "deviceType_id", user_owner_id) FROM stdin;
\.


--
-- Data for Name: battDB_devicetype; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_devicetype" (id, name, status, created_on, modified_on, attributes, notes, type, user_owner_id) FROM stdin;
\.


--
-- Data for Name: battDB_equipment; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_equipment" (id, attributes, "serialNo", type_id, status, user_owner_id, name, notes, modified_on, created_on) FROM stdin;
1	{}	1234	2	20	\N	Tom's GalvoTron 5000		2020-10-15 18:13:05.57799+01	2020-10-15 18:18:04.86402+01
\.


--
-- Data for Name: battDB_equipmenttype; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_equipmenttype" (id, attributes, status, user_owner_id, name, notes, modified_on, created_on) FROM stdin;
2	{"channels": 10}	20	\N	\N	\N	2020-10-15 18:13:05.616114+01	2020-10-15 18:18:04.884604+01
\.


--
-- Data for Name: battDB_experiment; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_experiment" (id, name, date, user_owner_id, status, protocol_id, "cellConfig_id", attributes, notes, modified_on, created_on) FROM stdin;
8	experiment	2020-08-05	1	edit	\N	\N	{}	\N	2020-10-15 18:13:05.703611+01	2020-10-15 18:18:04.905104+01
9	fooo	2020-08-05	1	edit	\N	\N	{}	\N	2020-10-15 18:13:05.703611+01	2020-10-15 18:18:04.905104+01
\.


--
-- Data for Name: battDB_experimentdatafile; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_experimentdatafile" (id, raw_data_file_id, experiment_id, machine_id, status, user_owner_id, attributes, name, notes, modified_on, created_on) FROM stdin;
\.


--
-- Data for Name: battDB_module; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_module" (device_ptr_id) FROM stdin;
\.


--
-- Data for Name: battDB_pack; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_pack" (device_ptr_id) FROM stdin;
\.


--
-- Data for Name: battDB_rawdatafile; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_rawdatafile" (id, status, attributes, raw_data_file, user_owner_id, name, notes, file_hash, modified_on, created_on) FROM stdin;
4	10	{}	raw_data_files/BioLogic_full_ozX9y9o.txt	1	foo		abf6e42283668f8ba9094a0f85411f64	2020-10-15 18:13:05.777506+01	2020-10-15 18:18:04.945437+01
6	10	{}	raw_data_files/200720_C-rate_test_Co5_cells_1-14_D128_CD1_VveSlEO.mpt	1	\N		5e68eaf524a479e401facdd53a22dc5a	2020-10-15 18:13:05.777506+01	2020-10-15 18:18:04.945437+01
8	10	{}	raw_data_files/mug.jpeg	1	\N	\N		2020-10-15 18:13:05.777506+01	2020-10-15 18:18:04.945437+01
\.


--
-- Data for Name: common_basemodelwithslug; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_basemodelwithslug (id, name, status, created_on, modified_on, attributes, notes, slug, user_owner_id) FROM stdin;
\.


--
-- Data for Name: common_org; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_org (id, website, is_mfg_cells, is_mfg_equip, is_publisher, is_research, manager_id, name) FROM stdin;
1	http://imperial.ac.uk	t	f	f	t	\N	Imperial College
\.


--
-- Data for Name: common_paper; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_paper (id, "DOI", year, title, url, publisher_id, attributes, status, user_owner_id, notes, "PDF", modified_on, created_on, slug) FROM stdin;
1	https://doi.org/10.1109/5.771073	2019	Toward unique identifiers	https://ieeexplore.ieee.org/document/771073	\N	{}	10	\N	.		2020-10-19 00:10:07.658318+01	2020-10-15 18:18:05.103148+01	toward-unique-identifiers-2019
\.


--
-- Data for Name: common_paperauthor; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_paperauthor (id, is_principal, author_id, paper_id) FROM stdin;
\.


--
-- Data for Name: common_person; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_person (id, org_id, user_id, "longName", "shortName") FROM stdin;
1	1	1	Tom Owen	T.Owen
2	\N	\N	nobby	n
\.


--
-- Data for Name: dfndb_compositionpart; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_compositionpart (id, amount, compound_id, material_id) FROM stdin;
2	2	3	1
3	2	4	1
1	6	5	1
4	1	2	2
5	1	1	3
\.


--
-- Data for Name: dfndb_compound; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_compound (id, formula, name, mass) FROM stdin;
1	Li	Lithium	0
3	Mg	Manganese	0
4	Co	Cobalt	0
2	C	Carbon	0
5	Ni	Nickel	0
\.


--
-- Data for Name: dfndb_data; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_data (id, paper_id, user_owner_id, attributes, status, name, notes, modified_on, created_on) FROM stdin;
1	1	1	{}	10	test foo	moo	2020-10-16	2020-10-16 18:01:43.737067+01
\.


--
-- Data for Name: dfndb_dataparameter; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_dataparameter (id, data_id, parameter_id, material_id, type, value) FROM stdin;
1	1	1	2	20	100
2	1	1	1	20	400
3	1	3	\N	30	\N
\.


--
-- Data for Name: dfndb_material; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_material (id, polymer, user_owner_id, type, attributes, status, name, notes, modified_on, created_on) FROM stdin;
2	1	1	1	{}	10	Graphite		2020-10-16	2020-10-16 15:05:13.815326+01
1	0	1	1	{}	10	NMC622		2020-10-16	2020-10-16 12:16:10.333468+01
3	0	1	2	{}	10	Lithium Metal		2020-10-16	2020-10-16 15:06:34.982964+01
\.


--
-- Data for Name: dfndb_method; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_method (id, type, description, user_owner_id, attributes, status, name, notes, modified_on, created_on) FROM stdin;
1	2		1	{}	10	DFN		2020-10-16	2020-10-16 14:09:50.498057+01
2	1		1	{}	10	GITT		2020-10-16	2020-10-16 14:10:00.357987+01
\.


--
-- Data for Name: dfndb_parameter; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_parameter (id, symbol, notes, unit_id, user_owner_id, attributes, status, name, modified_on, created_on) FROM stdin;
2	t		6	1	{}	10	Thickness	2020-10-16	2020-10-16 13:36:29.748252+01
3	C		9	1	{}	10	Capacity	2020-10-16	2020-10-16 13:51:37.090972+01
1	rP		10	\N	["boing", "boing"]	10	particle radius	2020-10-16	2020-10-16 13:02:34.855802+01
\.


--
-- Data for Name: dfndb_quantityunit; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_quantityunit (id, "quantityName", "quantitySymbol", "unitName", "unitSymbol", "is_SI_unit", related_scale, related_unit_id) FROM stdin;
6	Distance	d	metres	m	t	\N	\N
5	Current	I	Amps	A	t	\N	\N
4	Power	P	Watts	W	t	\N	\N
7	Distance	d	millimetres	mm	f	0.001	6
1	Voltage	V	Volts	V	t	\N	\N
3	Charge	Q	Coulombs	C	t	\N	\N
8	Energy	E	Joules	J	t	\N	\N
9	Capacity	C	Watt Hours	Wh	f	3600	8
10	Distance	d	nanometres	nm	f	1e-09	6
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-08-04 19:13:10.226362+01	1	foo	1	[{"added": {}}]	9	1
2	2020-08-04 19:25:35.516012+01	1	BorkCorp	1	[{"added": {}}]	4	1
3	2020-08-04 19:26:04.905071+01	1	foo	2	[{"changed": {"fields": ["manufacturer"]}}]	9	1
4	2020-08-04 19:27:53.921631+01	1	MyMembrane	1	[{"added": {}}]	2	1
5	2020-08-04 19:28:19.927154+01	1	MyLiPo	1	[{"added": {}}]	1	1
6	2020-08-04 19:41:57.989858+01	2	Maccor	1	[{"added": {}}]	4	1
7	2020-08-04 19:42:29.857145+01	1	GalvoTron 3000	1	[{"added": {}}]	16	1
8	2020-08-04 19:45:01.780472+01	2	GalvoTron 3000	1	[{"added": {}}]	16	1
9	2020-08-04 19:47:34.828985+01	1	Tom's GalvoTron 3000	1	[{"added": {}}]	3	1
10	2020-08-04 19:51:08.397906+01	1	PyBaMM example protocol	1	[{"added": {}}]	6	1
11	2020-08-04 19:52:01.270893+01	1	Tom's Lab	1	[{"added": {}}]	7	1
12	2020-08-04 19:52:35.233623+01	1	GalvoTron 3000	3		16	1
13	2020-08-04 19:52:52.127136+01	1	Tom's GalvoTron 3000	2	[{"changed": {"fields": ["type"]}}]	3	1
14	2020-08-04 19:54:28.563138+01	1	Experiment object (1)	1	[{"added": {}}]	8	1
15	2020-08-04 20:17:17.174324+01	1	4s	1	[{"added": {}}]	17	1
16	2020-08-04 20:26:50.203876+01	1	test test	2	[{"changed": {"fields": ["cells", "processed_data_file"]}}]	8	1
17	2020-08-04 20:36:45.200934+01	1	test test	2	[{"changed": {"fields": ["raw_data_file", "processed_data_file"]}}]	8	1
18	2020-08-05 13:09:30.332537+01	1	tom/test test/2020-08-04	3		8	1
19	2020-08-05 13:09:41.169381+01	6	tom/test test/2020-08-05	3		8	1
20	2020-08-05 13:09:41.245333+01	5	None/test test/2020-08-05	3		8	1
21	2020-08-05 13:09:41.270701+01	4	None/test test/2020-08-05	3		8	1
22	2020-08-05 13:15:42.946927+01	3	tom/test2/2020-08-05	2	[{"changed": {"fields": ["owner", "cells", "processed_data_file"]}}]	8	1
23	2020-08-05 13:15:47.904397+01	3	tom/test2/2020-08-05	2	[]	8	1
24	2020-08-05 13:17:32.85704+01	3	tom/test2/2020-08-05	3		8	1
25	2020-08-05 13:31:33.566157+01	8	tom/experiment/2020-08-05	1	[{"added": {}}]	8	1
26	2020-08-06 00:08:50.931818+01	9	tom/foo/2020-08-05	2	[{"changed": {"fields": ["cells"]}}]	8	1
27	2020-08-06 00:16:01.095768+01	9	tom/foo/2020-08-05	2	[]	8	1
28	2020-08-06 00:16:07.479654+01	9	tom/foo/2020-08-05	2	[]	8	1
29	2020-08-06 00:33:13.820898+01	9	tom/foo/2020-08-05	2	[]	8	1
30	2020-08-06 00:34:15.902395+01	9	tom/foo/2020-08-05	2	[{"changed": {"fields": ["analysis"]}}]	8	1
31	2020-08-06 00:34:26.132466+01	9	tom/foo/2020-08-05	2	[{"changed": {"fields": ["analysis"]}}]	8	1
32	2020-08-11 11:11:31.211091+01	2	jacql	1	[{"added": {}}]	12	1
33	2020-08-11 11:12:39.09724+01	2	jacql	2	[{"changed": {"fields": ["first_name", "last_name", "email", "is_staff", "is_superuser", "user_permissions"]}}]	12	1
34	2020-08-11 11:13:06.916932+01	1	Administrators	1	[{"added": {}}]	11	1
35	2020-08-11 11:14:31.126915+01	2	Experimenters	1	[{"added": {}}]	11	1
36	2020-08-12 11:25:52.862796+01	9	tom/foo/2020-08-05	2	[]	8	1
37	2020-08-12 11:26:41.764104+01	9	tom/foo/2020-08-05	2	[]	8	1
38	2020-08-12 15:11:16.810667+01	9	tom/foo/2020-08-05	2	[]	8	1
39	2020-08-12 15:11:41.598585+01	9	tom/foo/2020-08-05	2	[]	8	1
40	2020-08-12 15:11:42.044057+01	9	tom/foo/2020-08-05	2	[]	8	1
41	2020-08-12 15:14:51.399075+01	9	tom/fooo/2020-08-05	2	[{"changed": {"fields": ["name"]}}]	8	1
42	2020-08-12 15:15:48.104893+01	9	tom/fooo/2020-08-05	2	[]	8	1
43	2020-08-12 15:19:51.603273+01	9	tom/fooo/2020-08-05	2	[]	8	1
44	2020-08-12 15:25:19.660729+01	9	tom/fooo/2020-08-05	2	[]	8	1
45	2020-08-12 15:28:15.196452+01	9	tom/fooo/2020-08-05	2	[]	8	1
46	2020-08-12 15:34:24.734675+01	9	tom/fooo/2020-08-05	2	[]	8	1
47	2020-08-12 15:34:28.362297+01	8	tom/experiment/2020-08-05	2	[]	8	1
48	2020-08-13 09:53:36.7441+01	3	binbin	1	[{"added": {}}]	12	1
49	2020-08-13 09:54:53.286908+01	3	binbin	2	[{"changed": {"fields": ["first_name", "last_name", "is_staff", "groups"]}}]	12	1
50	2020-08-13 10:08:11.60325+01	1	BioLogic_full_u455xrV.txt	1	[{"added": {}}]	18	1
51	2020-08-13 11:32:39.18455+01	3	binbin	2	[{"changed": {"fields": ["is_superuser"]}}]	12	1
52	2020-08-13 11:45:05.248666+01	1	BioLogic_full_u455xrV.txt	2	[]	18	3
53	2020-08-13 11:45:09.003282+01	1	BioLogic_full_u455xrV.txt	2	[]	18	3
54	2020-08-13 11:45:59.648366+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	18	3
55	2020-08-13 11:46:07.851905+01	1	bio-logic-data-table.tsv	2	[{"changed": {"fields": ["raw_data_file"]}}]	18	1
56	2020-08-13 11:46:37.388125+01	1	BioLogic_full_Bq7ABsZ.txt	2	[{"changed": {"fields": ["raw_data_file"]}}]	18	1
57	2020-08-13 11:47:51.783604+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	1	[{"added": {}}]	18	3
58	2020-08-13 13:41:16.80162+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	2	[]	18	1
59	2020-08-13 13:44:28.732886+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	2	[]	18	1
60	2020-08-13 13:45:10.46911+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	2	[]	18	1
61	2020-08-13 14:56:13.246066+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_rRcvu3U.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	18	3
62	2020-08-13 15:42:26.567344+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_rRcvu3U.mpt	2	[]	18	1
63	2020-08-13 15:43:05.748529+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_xETlkXH.mpt	1	[{"added": {}}]	18	1
64	2020-08-13 15:43:11.157068+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_rRcvu3U.mpt	2	[]	18	1
65	2020-08-13 15:43:45.614216+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_oa7otTL.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	18	1
66	2020-08-13 15:46:34.261891+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lj6rngx.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	18	1
67	2020-08-13 15:52:59.611491+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lj6rngx.mpt	2	[]	18	1
68	2020-08-13 15:53:09.682091+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lvMpGzm.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	18	1
69	2020-08-13 15:54:23.605556+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lvMpGzm.mpt	2	[{"changed": {"fields": ["experiment"]}}]	18	1
70	2020-08-13 15:55:13.379716+01	9	tom/fooo/2020-08-05	2	[{"changed": {"fields": ["analysis"]}}]	8	1
71	2020-08-15 16:26:07.435613+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	1	[{"added": {}}]	19	1
72	2020-08-15 16:26:20.330113+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
73	2020-08-15 16:27:19.328572+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
74	2020-08-15 16:29:00.149786+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
75	2020-08-15 16:35:13.104076+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
76	2020-08-15 16:44:43.695498+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
77	2020-08-15 22:01:36.300505+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
78	2020-08-15 22:02:36.949811+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
79	2020-08-15 22:04:51.218447+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
80	2020-08-15 22:05:28.350057+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
81	2020-08-15 22:15:17.813728+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
82	2020-08-15 22:15:35.627463+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
84	2020-08-16 16:02:44.784119+01	6	rishi	1	[{"added": {}}]	12	1
85	2020-08-16 16:03:02.079082+01	6	rishi	2	[{"changed": {"fields": ["is_staff", "is_superuser"]}}]	12	1
86	2020-08-17 13:09:14.120233+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	19	1
87	2020-09-03 19:08:40.505196+01	1	Voltage	1	[{"added": {}}]	5	1
88	2020-09-03 19:08:49.55247+01	2	Current	1	[{"added": {}}]	5	1
89	2020-09-03 19:09:08.482438+01	3	Temperature	1	[{"added": {}}]	5	1
90	2020-09-03 19:09:18.249333+01	4	Time	1	[{"added": {}}]	5	1
91	2020-09-03 19:12:30.310237+01	4	Time	2	[{"changed": {"fields": ["unit"]}}]	5	1
92	2020-09-03 19:16:46.720441+01	4	Time/s	2	[{"changed": {"fields": ["unit_symbol"]}}]	5	1
93	2020-09-03 19:17:17.039241+01	3	Temperature/°C	2	[{"changed": {"fields": ["unit_symbol"]}}]	5	1
94	2020-09-03 19:17:33.724311+01	2	Current/A	2	[{"changed": {"fields": ["unit_name", "unit_symbol"]}}]	5	1
95	2020-09-03 19:17:40.814297+01	3	Temperature/°C	2	[{"changed": {"fields": ["unit_name"]}}]	5	1
96	2020-09-03 19:18:31.397625+01	1	Voltage/V	2	[{"changed": {"fields": ["unit_name", "unit_symbol"]}}]	5	1
97	2020-09-03 19:18:54.762396+01	5	Power/W	1	[{"added": {}}]	5	1
98	2020-09-03 20:56:48.721474+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_VhdOTOf.mpt	1	[{"added": {}}]	23	1
99	2020-09-04 00:49:08.152134+01	1	charging	1	[{"added": {}}]	22	1
100	2020-09-04 00:51:23.68365+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_VhdOTOf.mpt/1: charging	2	[]	22	1
101	2020-09-04 15:48:15.352707+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_VhdOTOf.mpt/1: charging	2	[{"changed": {"fields": ["ts_data"]}}]	22	1
102	2020-10-08 11:47:13.873693+01	6	rishi	3		12	1
103	2020-10-08 12:45:34.247115+01	1	Person object (1)	1	[{"added": {}}]	36	1
104	2020-10-08 12:55:45.05896+01	1	Imperial College	1	[{"added": {}}]	34	1
105	2020-10-08 12:59:15.023331+01	1	Imperial College	2	[]	34	1
106	2020-10-08 12:59:28.496262+01	1	Tom Owen	2	[{"changed": {"fields": ["Org"]}}]	36	1
107	2020-10-08 13:33:36.151723+01	7	test	1	[{"added": {}}]	12	1
108	2020-10-08 13:35:13.19285+01	7	test	2	[{"changed": {"fields": ["First name", "Last name", "User permissions"]}}]	12	1
109	2020-10-08 13:36:11.969134+01	7	test	2	[{"changed": {"fields": ["Staff status"]}}]	12	1
110	2020-10-08 14:28:58.653283+01	1	tom	2	[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]	12	1
111	2020-10-12 16:47:08.358212+01	1	Paper object (1)	1	[{"added": {}}]	35	1
112	2020-10-12 16:58:32.618011+01	3	BioLogic_full_SvcC6pn.txt	1	[{"added": {}}]	23	1
113	2020-10-12 16:58:45.778393+01	2		3		23	1
114	2020-10-12 21:36:22.3266+01	3	BioLogic_full_SvcC6pn.txt	3		23	1
115	2020-10-12 21:36:22.334348+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_VhdOTOf.mpt	3		23	1
116	2020-10-12 22:00:22.900391+01	1	ExperimentalApparatus object (1)	2	[]	7	1
117	2020-10-12 23:22:21.079795+01	1	ExperimentalApparatus object (1)	2	[{"changed": {"fields": ["Attributes"]}}]	7	1
118	2020-10-12 23:26:31.741966+01	1	None	2	[]	7	1
119	2020-10-14 14:47:38.831365+01	1	None	2	[]	35	1
120	2020-10-14 15:46:13.419807+01	1	52f1021a6e32e4202acab1c5c19f0067cc1ce38a	1	[{"added": {}}]	46	1
121	2020-10-15 12:49:42.377249+01	3	None	3		40	1
122	2020-10-15 12:49:57.048987+01	2	None	3		40	1
123	2020-10-15 12:49:57.053634+01	1	None	3		40	1
124	2020-10-15 13:04:19.151885+01	4	foo	1	[{"added": {}}]	40	1
125	2020-10-15 13:04:57.852735+01	4	foo	2	[{"changed": {"fields": ["Raw data file"]}}]	40	1
126	2020-10-15 13:05:13.279474+01	4	foo	2	[{"changed": {"fields": ["Raw data file"]}}]	40	1
127	2020-10-15 13:09:03.892766+01	6	None	1	[{"added": {}}]	40	1
128	2020-10-15 13:09:19.458002+01	6	None	2	[{"changed": {"fields": ["Raw data file"]}}]	40	1
129	2020-10-15 13:12:07.30048+01	6	None	2	[{"changed": {"fields": ["Raw data file"]}}]	40	1
130	2020-10-15 16:41:04.55752+01	1	Imperial College	2	[{"changed": {"fields": ["Name", "Status", "Notes", "Is research", "Is mfg cells", "Website"]}}]	34	1
131	2020-10-15 17:38:59.894418+01	1	Person object (1)	2	[{"changed": {"fields": ["Name", "User", "Org"]}}]	36	1
132	2020-10-15 17:55:03.068903+01	1	Tom's GalvoTron 5000	2	[{"changed": {"fields": ["Name"]}}]	3	1
133	2020-10-15 18:20:08.939864+01	1	foo-bar	2	[{"changed": {"fields": ["Publisher", "Authors"]}}]	35	1
134	2020-10-15 18:20:45.594399+01	1	foo-bar	2	[]	35	1
135	2020-10-15 18:21:05.262624+01	1	foo-bar	2	[]	35	1
136	2020-10-15 18:23:51.978293+01	1	toward-unique-identifiers2020	2	[]	35	1
137	2020-10-16 11:48:58.132684+01	1	Voltage/V	1	[{"added": {}}]	31	1
138	2020-10-16 11:49:10.766737+01	2	Current/I	1	[{"added": {}}]	31	1
139	2020-10-16 11:53:48.556196+01	2	QuantityUnit object (2)	3		31	1
140	2020-10-16 11:54:25.884777+01	1	Voltage/V	2	[{"changed": {"fields": ["UnitName", "UnitSymbol"]}}]	31	1
141	2020-10-16 11:54:43.876013+01	3	Charge/C	1	[{"added": {}}]	31	1
142	2020-10-16 11:56:30.363864+01	4	Power(P)/W	1	[{"added": {}}]	31	1
143	2020-10-16 11:56:50.860648+01	5	Current(I)/A	1	[{"added": {}}]	31	1
144	2020-10-16 12:01:35.832546+01	1	Lithium (Li)	1	[{"added": {}}]	28	1
145	2020-10-16 12:01:55.31366+01	2	Graphite (C)	1	[{"added": {}}]	28	1
146	2020-10-16 12:12:07.269505+01	1	Li6	1	[{"added": {}}]	27	1
147	2020-10-16 12:12:49.265806+01	3	Manganese (Mg)	1	[{"added": {}}]	28	1
148	2020-10-16 12:13:17.567964+01	4	Cobalt (Co)	1	[{"added": {}}]	28	1
149	2020-10-16 12:13:24.694319+01	2	Carbon (C)	2	[{"changed": {"fields": ["Name"]}}]	28	1
150	2020-10-16 12:13:54.865202+01	2	Mg2	1	[{"added": {}}]	27	1
151	2020-10-16 12:14:08.519116+01	3	Co2	1	[{"added": {}}]	27	1
152	2020-10-16 12:14:55.181487+01	5	Nickel (Ni)	1	[{"added": {}}]	28	1
153	2020-10-16 12:15:01.631788+01	4	Ni6	1	[{"added": {}}]	27	1
154	2020-10-16 12:16:10.339922+01	1	NMC622	1	[{"added": {}}]	29	1
155	2020-10-16 12:44:34.907919+01	1	NMC622	2	[{"added": {"name": "composition part", "object": "Li0"}}]	29	1
156	2020-10-16 12:45:00.824275+01	1	NMC622	2	[{"added": {"name": "composition part", "object": "Mg2"}}, {"added": {"name": "composition part", "object": "Co2"}}, {"changed": {"name": "composition part", "object": "Ni6", "fields": ["Compound", "Amount"]}}]	29	1
157	2020-10-16 12:54:56.11646+01	1	NMC622	2	[{"changed": {"name": "composition part", "object": "Ni7", "fields": ["Amount"]}}]	29	1
158	2020-10-16 12:55:00.733173+01	1	NMC622	2	[{"changed": {"name": "composition part", "object": "Ni6", "fields": ["Amount"]}}]	29	1
159	2020-10-16 13:02:19.57821+01	6	Distance (d) / m	1	[{"added": {}}]	31	1
160	2020-10-16 13:02:34.85802+01	1	particle radius: rP	1	[{"added": {}}]	32	1
161	2020-10-16 13:36:29.749178+01	2	Thickness: t	1	[{"added": {}}]	32	1
162	2020-10-16 13:43:10.094636+01	6	Distance (d) / m	2	[{"changed": {"fields": ["Is SI unit"]}}]	31	1
163	2020-10-16 13:43:16.5572+01	5	Current (I) / A	2	[{"changed": {"fields": ["Is SI unit"]}}]	31	1
164	2020-10-16 13:43:22.847922+01	4	Power (P) / W	2	[{"changed": {"fields": ["Is SI unit"]}}]	31	1
165	2020-10-16 13:45:42.452603+01	7	Distance (d) / mm	1	[{"added": {}}]	31	1
166	2020-10-16 13:46:01.828867+01	1	Voltage (V) / V	2	[{"changed": {"fields": ["Is SI unit"]}}]	31	1
167	2020-10-16 13:46:11.210912+01	3	Charge (Q) / C	2	[{"changed": {"fields": ["Is SI unit"]}}]	31	1
168	2020-10-16 13:50:43.775177+01	8	Energy (E) / J	1	[{"added": {}}]	31	1
169	2020-10-16 13:51:23.525296+01	9	Capacity (C) / Wh	1	[{"added": {}}]	31	1
170	2020-10-16 13:51:37.092029+01	3	Capacity: C / Wh	1	[{"added": {}}]	32	1
171	2020-10-16 14:09:50.499189+01	1	DFN	1	[{"added": {}}]	30	1
172	2020-10-16 14:10:00.35893+01	2	GITT	1	[{"added": {}}]	30	1
173	2020-10-16 14:56:03.399756+01	1	n	2	[{"changed": {"fields": ["User"]}}]	36	1
174	2020-10-16 14:59:39.38667+01	1	T.Owen	2	[{"changed": {"fields": ["LongName", "ShortName", "User"]}}]	36	1
175	2020-10-16 15:05:13.819015+01	2	Graphite	1	[{"added": {}}, {"added": {"name": "composition part", "object": "C1"}}]	29	1
176	2020-10-16 15:05:36.225971+01	1	NMC622	2	[{"changed": {"fields": ["User owner"]}}]	29	1
177	2020-10-16 15:06:34.98439+01	3	Lithium Metal	1	[{"added": {}}, {"added": {"name": "composition part", "object": "Li1"}}]	29	1
178	2020-10-16 18:01:43.739615+01	1	test foo	1	[{"added": {}}, {"added": {"name": "data parameter", "object": "DataParameter object (1)"}}]	33	1
179	2020-10-16 18:05:08.980434+01	1	test foo	2	[{"added": {"name": "data parameter", "object": "particle radius: rP / m"}}]	33	1
180	2020-10-16 18:07:52.509924+01	1	test foo	2	[{"changed": {"name": "data parameter", "object": "particle radius: rP / m", "fields": ["Value"]}}]	33	1
181	2020-10-16 18:09:41.262661+01	10	Particle Radius (rP) / nm	1	[{"added": {}}]	31	1
182	2020-10-16 18:10:14.091907+01	10	Distance (d) / nm	2	[{"changed": {"fields": ["QuantityName", "QuantitySymbol"]}}]	31	1
183	2020-10-16 18:10:26.756416+01	1	particle radius: rP / nm	2	[{"changed": {"fields": ["Unit"]}}]	32	1
184	2020-10-16 18:10:52.547143+01	1	particle radius: rP / nm	2	[]	32	1
185	2020-10-16 18:11:23.597568+01	1	particle radius: rP / nm	2	[{"changed": {"fields": ["Attributes"]}}]	32	1
186	2020-10-16 18:11:49.627821+01	1	particle radius: rP / nm	2	[{"changed": {"fields": ["Attributes"]}}]	32	1
187	2020-10-16 18:19:20.884585+01	1	test foo	2	[{"changed": {"name": "data parameter", "object": "particle radius: rP / nm", "fields": ["Value"]}}, {"changed": {"name": "data parameter", "object": "particle radius: rP / nm", "fields": ["Value"]}}]	33	1
188	2020-10-16 18:19:37.251546+01	1	test foo	2	[{"added": {"name": "data parameter", "object": "Capacity: C / Wh"}}, {"changed": {"name": "data parameter", "object": "particle radius: rP / nm", "fields": ["Type"]}}]	33	1
189	2020-10-16 18:21:10.81206+01	2	n	1	[{"added": {}}]	36	1
190	2020-10-16 18:21:59.880125+01	2	re-now-we-will-need-tin-hats-2020	1	[{"added": {}}, {"added": {"name": "paper author", "object": "PaperAuthor object (1)"}}]	35	1
191	2020-10-19 00:05:42.509708+01	2	re-now-we-will-need-tin-hats-2020	3		35	1
192	2020-10-19 00:06:26.891004+01	1	toward-unique-identifiers-2020	2	[]	35	1
193	2020-10-19 00:06:43.201108+01	1	toward-unique-identifiers-2020	2	[{"changed": {"fields": ["Notes"]}}]	35	1
194	2020-10-19 00:07:39.54622+01	1	toward-unique-identifiers-2020	2	[]	35	1
195	2020-10-19 00:09:05.032702+01	1	toward-unique-identifiers-2020	2	[]	35	1
196	2020-10-19 00:09:55.795814+01	1	toward-unique-identifiers-2020	2	[]	35	1
197	2020-10-19 00:10:07.659737+01	1	toward-unique-identifiers-2019	2	[{"changed": {"fields": ["Year"]}}]	35	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	battDB	cell
2	battDB	cellseparator
3	battDB	equipment
4	battDB	manufacturer
5	battDB	signaltype
6	battDB	testprotocol
7	battDB	experimentalapparatus
8	battDB	experiment
9	battDB	cellbatch
10	auth	permission
11	auth	group
12	auth	user
13	contenttypes	contenttype
14	admin	logentry
15	sessions	session
16	battDB	equipmenttype
17	battDB	cellconfig
18	battDB	experimentresult
19	battDB	experimentdata
20	battDB	ec_cycle
21	battDB	celltype
22	battDB	datarange
23	battDB	experimentdatafile
24	django_plotly_dash	dashapp
25	django_plotly_dash	statelessapp
26	dfndb	paper
27	dfndb	compositionpart
28	dfndb	compound
29	dfndb	material
30	dfndb	method
31	dfndb	quantityunit
32	dfndb	parameter
33	dfndb	data
34	common	org
35	common	paper
36	common	person
37	battDB	devicetype
38	battDB	devicebatch
39	battDB	device
40	battDB	rawdatafile
41	battDB	apparatusequipment
42	common	devicetype
43	common	device
44	common	batch
45	authtoken	token
46	authtoken	tokenproxy
47	battDB	batch
48	dfndb	dataparameter
49	common	paperauthor
50	battDB	deviceconfignode
51	battDB	deviceconfig
52	common	basemodelwithslug
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-08-04 19:06:03.247234+01
2	auth	0001_initial	2020-08-04 19:06:03.581176+01
3	battDB	0001_initial	2020-08-04 19:06:04.868539+01
4	admin	0001_initial	2020-08-04 19:07:21.857673+01
5	admin	0002_logentry_remove_auto_add	2020-08-04 19:07:21.984528+01
6	admin	0003_logentry_add_action_flag_choices	2020-08-04 19:07:22.066678+01
7	contenttypes	0002_remove_content_type_name	2020-08-04 19:07:22.128877+01
8	auth	0002_alter_permission_name_max_length	2020-08-04 19:07:22.180271+01
9	auth	0003_alter_user_email_max_length	2020-08-04 19:07:22.241102+01
10	auth	0004_alter_user_username_opts	2020-08-04 19:07:22.298791+01
11	auth	0005_alter_user_last_login_null	2020-08-04 19:07:22.360328+01
12	auth	0006_require_contenttypes_0002	2020-08-04 19:07:22.413536+01
13	auth	0007_alter_validators_add_error_messages	2020-08-04 19:07:22.463504+01
14	auth	0008_alter_user_username_max_length	2020-08-04 19:07:22.555198+01
15	auth	0009_alter_user_last_name_max_length	2020-08-04 19:07:22.604918+01
16	auth	0010_alter_group_name_max_length	2020-08-04 19:07:22.665178+01
17	auth	0011_update_proxy_permissions	2020-08-04 19:07:22.755407+01
18	sessions	0001_initial	2020-08-04 19:07:22.913476+01
19	battDB	0002_auto_20200804_1838	2020-08-04 19:38:40.04937+01
20	battDB	0003_equipment_type	2020-08-04 19:39:59.74901+01
21	battDB	0004_equipmenttype_manufacturer	2020-08-04 19:41:29.155848+01
22	battDB	0005_auto_20200804_1856	2020-08-04 19:57:00.082477+01
23	battDB	0006_experimentalapparatus_photo	2020-08-04 20:01:27.431661+01
24	battDB	0007_auto_20200804_1915	2020-08-04 20:15:13.651658+01
25	battDB	0008_experimentalapparatus_cellconfig	2020-08-04 20:15:40.10692+01
26	battDB	0009_auto_20200804_1920	2020-08-04 20:20:38.723312+01
27	battDB	0010_experiment_processed_data_file	2020-08-04 20:21:22.617814+01
28	battDB	0011_auto_20200804_1926	2020-08-04 20:26:18.143222+01
29	battDB	0012_cell_separator	2020-08-05 11:58:54.136899+01
30	battDB	0013_auto_20200805_1146	2020-08-05 12:46:57.293892+01
31	battDB	0014_auto_20200805_1214	2020-08-05 13:15:06.796335+01
32	battDB	0015_auto_20200812_1541	2020-08-12 16:41:42.949931+01
33	battDB	0016_auto_20200812_1605	2020-08-13 09:31:29.775636+01
34	battDB	0017_experiment_status	2020-08-13 09:31:29.869074+01
35	battDB	0018_auto_20200812_1632	2020-08-13 09:31:29.927666+01
36	battDB	0019_auto_20200812_1633	2020-08-13 09:31:30.001311+01
37	battDB	0020_auto_20200812_1646	2020-08-13 09:31:30.051582+01
38	battDB	0021_auto_20200813_1015	2020-08-13 11:15:17.881701+01
39	battDB	0022_auto_20200815_1426	2020-08-15 15:26:51.57265+01
40	battDB	0023_experimentdata_data	2020-08-15 16:24:19.638608+01
41	battDB	0024_auto_20200815_1611	2020-08-15 17:11:53.938322+01
42	battDB	0025_remove_experimentdata_data	2020-08-15 22:01:17.527853+01
43	battDB	0026_experimentdata_data	2020-08-15 22:01:17.694183+01
44	battDB	0026_ec_cycle	2020-08-16 14:22:07.595025+01
45	battDB	0027_auto_20200816_1322	2020-08-16 14:22:33.590537+01
46	battDB	0028_experimentdata_data	2020-08-16 14:23:43.189628+01
47	battDB	0029_remove_experimentdata_data	2020-08-16 14:24:00.605166+01
48	battDB	0030_experimentdata_data	2020-08-16 14:24:16.021639+01
49	battDB	0031_auto_20200816_1357	2020-08-16 14:57:47.206087+01
50	battDB	0032_auto_20200816_1432	2020-08-16 15:32:53.628752+01
51	battDB	0033_auto_20200818_1355	2020-08-18 14:55:49.616605+01
52	battDB	0034_experimentdatafile_machine	2020-08-18 15:33:40.748065+01
53	battDB	0035_datarange_file_offset	2020-08-18 15:35:57.135728+01
56	battDB	0036_auto_20200903_1753	2020-09-03 18:53:52.800881+01
57	battDB	0037_signaltype_symbol	2020-09-03 19:08:20.783023+01
58	battDB	0038_signaltype_unit	2020-09-03 19:12:20.35129+01
59	battDB	0039_auto_20200903_1814	2020-09-03 19:14:18.319432+01
60	battDB	0040_auto_20200903_1816	2020-09-03 19:16:37.671965+01
61	auth	0012_alter_user_first_name_max_length	2020-10-07 13:25:56.568632+01
62	battDB	0041_auto_20200908_1119	2020-10-07 13:25:56.683129+01
63	dfndb	0001_initial	2020-10-08 10:26:11.274739+01
64	dfndb	0002_auto_20201001_0930	2020-10-08 10:26:11.376124+01
65	dfndb	0003_material_polymer	2020-10-08 10:26:11.444844+01
66	dfndb	0004_auto_20201001_1123	2020-10-08 10:26:11.5701+01
67	dfndb	0005_auto_20201001_1131	2020-10-08 10:26:11.738805+01
68	dfndb	0006_auto_20201001_2335	2020-10-08 10:26:11.779157+01
69	common	0001_initial	2020-10-08 12:32:53.147931+01
70	dfndb	0007_auto_20201008_1132	2020-10-08 12:32:53.269593+01
71	common	0002_paper_org_owners	2020-10-08 13:06:18.210671+01
72	common	0003_auto_20201008_1242	2020-10-08 13:42:20.911176+01
73	common	0004_auto_20201008_1321	2020-10-08 14:22:04.37714+01
74	common	0005_auto_20201008_1430	2020-10-08 15:30:10.847876+01
75	dfndb	0002_auto_20201008_1430	2020-10-08 15:30:10.927234+01
76	battDB	0042_auto_20201010_1321	2020-10-10 14:23:03.214408+01
77	battDB	0043_auto_20201010_1322	2020-10-10 14:23:03.274774+01
78	common	0006_auto_20201011_1314	2020-10-11 14:15:00.313579+01
79	dfndb	0003_auto_20201011_1314	2020-10-11 14:15:00.400816+01
80	battDB	0044_auto_20201012_1126	2020-10-12 12:26:20.712703+01
81	common	0007_auto_20201012_1126	2020-10-12 12:26:21.042747+01
82	dfndb	0004_auto_20201012_1126	2020-10-12 12:26:21.483319+01
83	battDB	0045_auto_20201012_1549	2020-10-12 16:49:36.863661+01
84	common	0008_auto_20201012_1549	2020-10-12 16:49:37.044272+01
85	dfndb	0005_auto_20201012_1549	2020-10-12 16:49:37.345337+01
86	battDB	0046_auto_20201012_1556	2020-10-12 16:56:29.859339+01
87	battDB	0047_auto_20201012_1623	2020-10-12 21:36:37.650327+01
88	common	0009_auto_20201012_1623	2020-10-12 21:36:37.787207+01
89	dfndb	0006_auto_20201012_1623	2020-10-12 21:36:37.885508+01
90	battDB	0048_auto_20201012_2059	2020-10-12 21:59:49.589668+01
91	battDB	0049_remove_experimentalapparatus_testequipment	2020-10-12 22:23:20.598164+01
92	battDB	0050_experimentalapparatus_testequipment	2020-10-12 22:23:33.535437+01
93	battDB	0051_auto_20201012_2225	2020-10-12 23:25:25.769035+01
94	common	0010_auto_20201012_2225	2020-10-12 23:25:25.943231+01
95	dfndb	0007_auto_20201012_2225	2020-10-12 23:25:26.102311+01
96	battDB	0052_auto_20201012_2229	2020-10-12 23:29:58.35459+01
97	battDB	0053_auto_20201013_2250	2020-10-13 23:51:16.733107+01
98	common	0011_auto_20201013_2250	2020-10-13 23:51:16.981289+01
99	dfndb	0008_auto_20201013_2250	2020-10-13 23:51:17.183785+01
100	battDB	0054_auto_20201014_1344	2020-10-14 14:44:46.791122+01
101	common	0012_paper_pdf	2020-10-14 14:44:46.819836+01
102	authtoken	0001_initial	2020-10-14 15:45:36.759056+01
103	authtoken	0002_auto_20160226_1747	2020-10-14 15:45:36.895847+01
104	authtoken	0003_tokenproxy	2020-10-14 15:45:36.901198+01
105	battDB	0055_auto_20201015_1051	2020-10-15 11:51:43.38991+01
106	battDB	0056_rawdatafile_file_hash	2020-10-15 12:49:10.432527+01
107	battDB	0057_auto_20201015_1150	2020-10-15 12:50:16.592926+01
108	common	0013_auto_20201015_1636	2020-10-15 17:36:19.222616+01
109	battDB	0058_auto_20201015_1653	2020-10-15 17:53:34.719059+01
110	common	0014_auto_20201015_1653	2020-10-15 17:53:34.847147+01
111	dfndb	0009_auto_20201015_1653	2020-10-15 17:53:34.928726+01
112	battDB	0059_auto_20201015_1658	2020-10-15 17:58:15.673496+01
113	battDB	0059_auto_20201015_1703	2020-10-15 18:07:23.178451+01
114	battDB	0060_auto_20201015_1704	2020-10-15 18:07:23.653619+01
115	common	0015_auto_20201015_1710	2020-10-15 18:10:46.94928+01
116	battDB	0061_auto_20201015_1712	2020-10-15 18:12:12.833484+01
117	common	0016_auto_20201015_1712	2020-10-15 18:12:12.996449+01
118	dfndb	0009_auto_20201015_1712	2020-10-15 18:12:13.134555+01
119	battDB	0062_auto_20201015_1713	2020-10-15 18:13:05.81665+01
120	common	0017_auto_20201015_1713	2020-10-15 18:13:05.982766+01
121	dfndb	0010_auto_20201015_1713	2020-10-15 18:13:54.587799+01
122	battDB	0063_auto_20201015_1716	2020-10-15 18:16:31.085157+01
123	common	0018_auto_20201015_1716	2020-10-15 18:16:31.219126+01
124	dfndb	0011_auto_20201015_1716	2020-10-15 18:17:11.808442+01
125	battDB	0064_auto_20201015_1718	2020-10-15 18:18:04.966791+01
126	common	0019_auto_20201015_1718	2020-10-15 18:18:05.104823+01
127	dfndb	0012_auto_20201015_1718	2020-10-15 18:18:05.192766+01
128	battDB	0065_signaltype	2020-10-16 00:12:39.106474+01
129	common	0020_auto_20201015_2312	2020-10-16 00:12:39.236936+01
130	common	0021_auto_20201015_2316	2020-10-16 00:16:20.435802+01
131	battDB	0066_auto_20201015_2316	2020-10-16 00:16:20.638273+01
132	battDB	0067_auto_20201015_2320	2020-10-16 00:20:18.580532+01
133	battDB	0068_device_devicebatch	2020-10-16 00:20:42.632764+01
134	battDB	0069_auto_20201015_2330	2020-10-16 00:30:57.645477+01
135	battDB	0070_auto_20201015_2331	2020-10-16 00:31:27.76573+01
136	dfndb	0013_auto_20201016_1054	2020-10-16 11:54:07.156866+01
137	dfndb	0014_auto_20201016_1109	2020-10-16 12:09:55.976777+01
138	dfndb	0015_auto_20201016_1116	2020-10-16 12:16:59.203382+01
139	dfndb	0016_auto_20201016_1132	2020-10-16 12:32:26.010252+01
140	dfndb	0017_auto_20201016_1136	2020-10-16 12:36:24.479414+01
141	dfndb	0018_auto_20201016_1201	2020-10-16 13:01:19.484117+01
142	dfndb	0019_remove_data_parameter	2020-10-16 13:06:29.293922+01
143	dfndb	0020_auto_20201016_1211	2020-10-16 13:11:28.311338+01
144	common	0022_remove_paper_authors	2020-10-16 13:16:23.050458+01
145	common	0023_auto_20201016_1219	2020-10-16 13:19:09.07709+01
146	dfndb	0021_auto_20201016_1234	2020-10-16 13:34:51.343923+01
147	dfndb	0022_auto_20201016_1242	2020-10-16 13:42:34.407659+01
148	dfndb	0023_auto_20201016_1245	2020-10-16 13:45:39.468389+01
149	common	0024_auto_20201016_1354	2020-10-16 14:54:54.508138+01
150	dfndb	0024_auto_20201016_1354	2020-10-16 14:54:54.547899+01
151	common	0025_auto_20201016_1404	2020-10-16 15:07:48.463978+01
152	dfndb	0025_auto_20201016_1404	2020-10-16 15:07:48.541286+01
153	dfndb	0026_auto_20201016_1655	2020-10-16 18:01:00.986475+01
154	dfndb	0027_remove_data_data	2020-10-16 18:01:01.010976+01
155	dfndb	0028_auto_20201016_1706	2020-10-16 18:06:25.437249+01
156	dfndb	0029_auto_20201016_1707	2020-10-16 18:07:19.779871+01
157	battDB	0071_module_pack	2020-10-17 18:48:51.820527+01
158	battDB	0071_auto_20201017_2350	2020-10-18 00:50:28.622411+01
159	battDB	0072_auto_20201018_2215	2020-10-18 23:15:26.063333+01
160	battDB	0073_remove_deviceconfignode_type	2020-10-18 23:18:06.404016+01
161	battDB	0074_delete_deviceconfignode	2020-10-18 23:18:34.948709+01
162	battDB	0075_auto_20201018_2254	2020-10-18 23:55:01.062778+01
163	dfndb	0030_auto_20201018_2254	2020-10-18 23:55:01.23362+01
164	common	0026_auto_20201018_2306	2020-10-19 00:06:15.484676+01
165	battDB	0076_auto_20201019_1209	2020-10-19 13:09:18.173645+01
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
kznm4zgwzhdw2pczzmghrq040i9bcghc	ODkzNGRjMTU3YjY1NTAxMDE2MGU5NGRmNzU3ZWQ1YjYzOGEwMGJjNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZDc3MzRjOGIwMDg0NmM4NGU3Nzg1ZGZiZjc3ZTk4ODBhMWE3OWFiIn0=	2020-08-25 11:09:00.092024+01
h2aulckzjnz6unc9858uvjsm0l9vkte3	ODkzNGRjMTU3YjY1NTAxMDE2MGU5NGRmNzU3ZWQ1YjYzOGEwMGJjNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZDc3MzRjOGIwMDg0NmM4NGU3Nzg1ZGZiZjc3ZTk4ODBhMWE3OWFiIn0=	2020-08-25 11:09:23.656754+01
gt0dz60n04ed1vrqtlexu7jdi7gptr49	YzU3OGZjOTUyOGIwMWRkNTRlNmU5YjdiMDQ2Mzk5ZGQ4ZWFmM2VlMDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4YzIxYTM2MzE3ZDI0ODU0MmMwODViZDc5NGVjYzFkMTRmMGE3NmJkIn0=	2020-08-27 10:56:28.22271+01
bjvejex0ig5m2h3m5hr259xggqcz3who	ODkzNGRjMTU3YjY1NTAxMDE2MGU5NGRmNzU3ZWQ1YjYzOGEwMGJjNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZDc3MzRjOGIwMDg0NmM4NGU3Nzg1ZGZiZjc3ZTk4ODBhMWE3OWFiIn0=	2020-09-17 19:02:52.232582+01
cyyrb7merwtxo7dcsbv0cgqmwccnwh8d	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kQRx2:1XeV7lhO2h-Cmtkg1ptczSM0aWNs1M7WLEN5Tzm-pIU	2020-10-22 10:11:04.359096+01
haqcurfqstoy8ys4evb16c4zer8xs1lc	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kQVAL:iSngFIWICRX_JMTDzaTgNLmNR4npexx4OOSyqzT0sBc	2020-10-22 13:37:01.400797+01
9n5s8vuiaybs4f16zd2ihvnybnmmowy2	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kQVqO:20Y9Qbxw_AkXrCn32uTJZN1QvCTJsKjEpMWC-SDA4WA	2020-10-22 14:20:28.773308+01
q9avywvdm0hqnyxnd71cf15khj1f23dk	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kRb9W:KueNOMangHXfaAINnKiYugVGf3zjBpSz8Fg9KXljp5Y	2020-10-25 13:12:42.132228+00
ec6pd3vza131tw3s8hdhrtbact9c39od	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kSH0S:YMIC2rs4Cs26Vsvb4iamHDpi6h85vKutEpU3Qhs0MXE	2020-10-27 09:54:08.874351+00
mb8xezkfh12vyv80crcv462o2wfaiydq	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kTtA4:Z6s8v3V8CFqtgrlLW5XlMF_zvKSxJzgktRZ9VxCOm4M	2020-10-31 20:50:44.256949+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 112, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 208, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 7, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 104, true);


--
-- Name: battDB_cellconfig_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_cellconfig_id_seq"', 1, true);


--
-- Name: battDB_datarange_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_datarange_id_seq"', 1, true);


--
-- Name: battDB_devicebatch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_devicebatch_id_seq"', 1, false);


--
-- Name: battDB_deviceconfig_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_deviceconfig_id_seq"', 1, false);


--
-- Name: battDB_deviceconfignode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_deviceconfignode_id_seq"', 1, false);


--
-- Name: battDB_devicetype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_devicetype_id_seq"', 1, false);


--
-- Name: battDB_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_equipment_id_seq"', 1, true);


--
-- Name: battDB_equipmenttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_equipmenttype_id_seq"', 2, true);


--
-- Name: battDB_experiment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_experiment_id_seq"', 9, true);


--
-- Name: battDB_experimentdatafile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_experimentdatafile_id_seq"', 3, true);


--
-- Name: battDB_rawdatafile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_rawdatafile_id_seq"', 12, true);


--
-- Name: common_basemodelwithslug_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_basemodelwithslug_id_seq', 1, false);


--
-- Name: common_org_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_org_id_seq', 1, true);


--
-- Name: common_paper_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_paper_id_seq', 2, true);


--
-- Name: common_paperauthor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_paperauthor_id_seq', 1, true);


--
-- Name: common_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_person_id_seq', 2, true);


--
-- Name: dfndb_compositionpart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_compositionpart_id_seq', 5, true);


--
-- Name: dfndb_compound_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_compound_id_seq', 5, true);


--
-- Name: dfndb_data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_data_id_seq', 1, true);


--
-- Name: dfndb_dataparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_dataparameter_id_seq', 3, true);


--
-- Name: dfndb_material_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_material_id_seq', 3, true);


--
-- Name: dfndb_method_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_method_id_seq', 2, true);


--
-- Name: dfndb_parameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_parameter_id_seq', 3, true);


--
-- Name: dfndb_quantityunit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_quantityunit_id_seq', 10, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 197, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 52, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 165, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: battDB_cellconfig battDB_cellconfig_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_cellconfig"
    ADD CONSTRAINT "battDB_cellconfig_pkey" PRIMARY KEY (id);


--
-- Name: battDB_datarange battDB_datarange_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datarange"
    ADD CONSTRAINT "battDB_datarange_pkey" PRIMARY KEY (id);


--
-- Name: battDB_devicebatch battDB_devicebatch_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_pkey" PRIMARY KEY (id);


--
-- Name: battDB_deviceconfig battDB_deviceconfig_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfig"
    ADD CONSTRAINT "battDB_deviceconfig_pkey" PRIMARY KEY (id);


--
-- Name: battDB_deviceconfignode battDB_deviceconfignode_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfignode"
    ADD CONSTRAINT "battDB_deviceconfignode_pkey" PRIMARY KEY (id);


--
-- Name: battDB_devicetype battDB_devicetype_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicetype"
    ADD CONSTRAINT "battDB_devicetype_pkey" PRIMARY KEY (id);


--
-- Name: battDB_equipment battDB_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_pkey" PRIMARY KEY (id);


--
-- Name: battDB_equipmenttype battDB_equipmenttype_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipmenttype"
    ADD CONSTRAINT "battDB_equipmenttype_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experiment battDB_experiment_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experimentdatafile battDB_experimentdatafile_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdatafile_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experimentdatafile battDB_experimentdatafile_raw_data_file_id_91752398_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdatafile_raw_data_file_id_91752398_uniq" UNIQUE (raw_data_file_id);


--
-- Name: battDB_module battDB_module_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_module"
    ADD CONSTRAINT "battDB_module_pkey" PRIMARY KEY (device_ptr_id);


--
-- Name: battDB_pack battDB_pack_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_pack"
    ADD CONSTRAINT "battDB_pack_pkey" PRIMARY KEY (device_ptr_id);


--
-- Name: battDB_rawdatafile battDB_rawdatafile_file_hash_d0cce686_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_rawdatafile"
    ADD CONSTRAINT "battDB_rawdatafile_file_hash_d0cce686_uniq" UNIQUE (file_hash);


--
-- Name: battDB_rawdatafile battDB_rawdatafile_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_rawdatafile"
    ADD CONSTRAINT "battDB_rawdatafile_pkey" PRIMARY KEY (id);


--
-- Name: common_basemodelwithslug common_basemodelwithslug_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_basemodelwithslug
    ADD CONSTRAINT common_basemodelwithslug_pkey PRIMARY KEY (id);


--
-- Name: common_basemodelwithslug common_basemodelwithslug_slug_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_basemodelwithslug
    ADD CONSTRAINT common_basemodelwithslug_slug_key UNIQUE (slug);


--
-- Name: common_org common_org_name_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_org
    ADD CONSTRAINT common_org_name_key UNIQUE (name);


--
-- Name: common_org common_org_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_org
    ADD CONSTRAINT common_org_pkey PRIMARY KEY (id);


--
-- Name: common_paper common_paper_DOI_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paper
    ADD CONSTRAINT "common_paper_DOI_key" UNIQUE ("DOI");


--
-- Name: common_paper common_paper_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paper
    ADD CONSTRAINT common_paper_pkey PRIMARY KEY (id);


--
-- Name: common_paper common_paper_slug_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paper
    ADD CONSTRAINT common_paper_slug_key UNIQUE (slug);


--
-- Name: common_paperauthor common_paperauthor_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paperauthor
    ADD CONSTRAINT common_paperauthor_pkey PRIMARY KEY (id);


--
-- Name: common_person common_person_longName_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person
    ADD CONSTRAINT "common_person_longName_key" UNIQUE ("longName");


--
-- Name: common_person common_person_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person
    ADD CONSTRAINT common_person_pkey PRIMARY KEY (id);


--
-- Name: common_person common_person_shortName_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person
    ADD CONSTRAINT "common_person_shortName_key" UNIQUE ("shortName");


--
-- Name: common_person common_person_user_id_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person
    ADD CONSTRAINT common_person_user_id_key UNIQUE (user_id);


--
-- Name: dfndb_compositionpart dfndb_compositionpart_compound_id_amount_mater_69ebccd8_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compositionpart
    ADD CONSTRAINT dfndb_compositionpart_compound_id_amount_mater_69ebccd8_uniq UNIQUE (compound_id, amount, material_id);


--
-- Name: dfndb_compositionpart dfndb_compositionpart_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compositionpart
    ADD CONSTRAINT dfndb_compositionpart_pkey PRIMARY KEY (id);


--
-- Name: dfndb_compound dfndb_compound_name_formula_fe305ecc_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compound
    ADD CONSTRAINT dfndb_compound_name_formula_fe305ecc_uniq UNIQUE (name, formula);


--
-- Name: dfndb_compound dfndb_compound_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compound
    ADD CONSTRAINT dfndb_compound_pkey PRIMARY KEY (id);


--
-- Name: dfndb_data dfndb_data_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_data
    ADD CONSTRAINT dfndb_data_pkey PRIMARY KEY (id);


--
-- Name: dfndb_dataparameter dfndb_dataparameter_data_id_parameter_id_mat_db552193_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_dataparameter
    ADD CONSTRAINT dfndb_dataparameter_data_id_parameter_id_mat_db552193_uniq UNIQUE (data_id, parameter_id, material_id);


--
-- Name: dfndb_dataparameter dfndb_dataparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_dataparameter
    ADD CONSTRAINT dfndb_dataparameter_pkey PRIMARY KEY (id);


--
-- Name: dfndb_material dfndb_material_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_material
    ADD CONSTRAINT dfndb_material_pkey PRIMARY KEY (id);


--
-- Name: dfndb_method dfndb_method_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_method
    ADD CONSTRAINT dfndb_method_pkey PRIMARY KEY (id);


--
-- Name: dfndb_parameter dfndb_parameter_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_parameter
    ADD CONSTRAINT dfndb_parameter_pkey PRIMARY KEY (id);


--
-- Name: dfndb_parameter dfndb_parameter_symbol_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_parameter
    ADD CONSTRAINT dfndb_parameter_symbol_key UNIQUE (symbol);


--
-- Name: dfndb_quantityunit dfndb_quantityunit_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_quantityunit
    ADD CONSTRAINT dfndb_quantityunit_pkey PRIMARY KEY (id);


--
-- Name: dfndb_quantityunit dfndb_quantityunit_quantityName_unitSymbol_770a6f9f_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_quantityunit
    ADD CONSTRAINT "dfndb_quantityunit_quantityName_unitSymbol_770a6f9f_uniq" UNIQUE ("quantityName", "unitSymbol");


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: battDB_cellconfig_user_owner_id_474eea19; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_cellconfig_user_owner_id_474eea19" ON public."battDB_cellconfig" USING btree (user_owner_id);


--
-- Name: battDB_datarange_dataFile_id_ea79f7c6; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_datarange_dataFile_id_ea79f7c6" ON public."battDB_datarange" USING btree ("dataFile_id");


--
-- Name: battDB_datarange_user_owner_id_a458c111; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_datarange_user_owner_id_a458c111" ON public."battDB_datarange" USING btree (user_owner_id);


--
-- Name: battDB_devicebatch_device_type_id_f4cf37bf; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_device_type_id_f4cf37bf" ON public."battDB_devicebatch" USING btree (device_type_id);


--
-- Name: battDB_devicebatch_manufacturer_id_85675f1a; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_manufacturer_id_85675f1a" ON public."battDB_devicebatch" USING btree (manufacturer_id);


--
-- Name: battDB_devicebatch_user_owner_id_a17097e8; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_user_owner_id_a17097e8" ON public."battDB_devicebatch" USING btree (user_owner_id);


--
-- Name: battDB_deviceconfig_user_owner_id_9f82fb32; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfig_user_owner_id_9f82fb32" ON public."battDB_deviceconfig" USING btree (user_owner_id);


--
-- Name: battDB_deviceconfignode_deviceConfig_id_5f8801f8; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfignode_deviceConfig_id_5f8801f8" ON public."battDB_deviceconfignode" USING btree ("deviceConfig_id");


--
-- Name: battDB_deviceconfignode_deviceType_id_5184063c; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfignode_deviceType_id_5184063c" ON public."battDB_deviceconfignode" USING btree ("deviceType_id");


--
-- Name: battDB_deviceconfignode_user_owner_id_eebcdcc8; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfignode_user_owner_id_eebcdcc8" ON public."battDB_deviceconfignode" USING btree (user_owner_id);


--
-- Name: battDB_devicetype_user_owner_id_e20a07ac; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicetype_user_owner_id_e20a07ac" ON public."battDB_devicetype" USING btree (user_owner_id);


--
-- Name: battDB_equipment_type_id_92966c47; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_type_id_92966c47" ON public."battDB_equipment" USING btree (type_id);


--
-- Name: battDB_equipment_user_owner_id_bbb9f49e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_user_owner_id_bbb9f49e" ON public."battDB_equipment" USING btree (user_owner_id);


--
-- Name: battDB_equipmenttype_user_owner_id_366e387f; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipmenttype_user_owner_id_366e387f" ON public."battDB_equipmenttype" USING btree (user_owner_id);


--
-- Name: battDB_experiment_cellConfig_id_2d8d4638; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_cellConfig_id_2d8d4638" ON public."battDB_experiment" USING btree ("cellConfig_id");


--
-- Name: battDB_experiment_name_4a1b5666; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_name_4a1b5666" ON public."battDB_experiment" USING btree (name);


--
-- Name: battDB_experiment_name_4a1b5666_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_name_4a1b5666_like" ON public."battDB_experiment" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_experiment_owner_id_ebf94468; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_owner_id_ebf94468" ON public."battDB_experiment" USING btree (user_owner_id);


--
-- Name: battDB_experiment_protocol_id_ed0e9fcd; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_protocol_id_ed0e9fcd" ON public."battDB_experiment" USING btree (protocol_id);


--
-- Name: battDB_experimentdatafile_experiment_id_de169b40; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_experiment_id_de169b40" ON public."battDB_experimentdatafile" USING btree (experiment_id);


--
-- Name: battDB_experimentdatafile_machine_id_383367b5; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_machine_id_383367b5" ON public."battDB_experimentdatafile" USING btree (machine_id);


--
-- Name: battDB_experimentdatafile_user_owner_id_f8f951f2; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_user_owner_id_f8f951f2" ON public."battDB_experimentdatafile" USING btree (user_owner_id);


--
-- Name: battDB_rawdatafile_file_hash_d0cce686_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_rawdatafile_file_hash_d0cce686_like" ON public."battDB_rawdatafile" USING btree (file_hash varchar_pattern_ops);


--
-- Name: battDB_rawdatafile_user_owner_id_90ad71dd; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_rawdatafile_user_owner_id_90ad71dd" ON public."battDB_rawdatafile" USING btree (user_owner_id);


--
-- Name: common_basemodelwithslug_slug_1375b2f2_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_basemodelwithslug_slug_1375b2f2_like ON public.common_basemodelwithslug USING btree (slug varchar_pattern_ops);


--
-- Name: common_basemodelwithslug_user_owner_id_b2ac42c9; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_basemodelwithslug_user_owner_id_b2ac42c9 ON public.common_basemodelwithslug USING btree (user_owner_id);


--
-- Name: common_org_name_062cae2a_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_org_name_062cae2a_like ON public.common_org USING btree (name varchar_pattern_ops);


--
-- Name: common_org_user_owner_id_353d3267; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_org_user_owner_id_353d3267 ON public.common_org USING btree (manager_id);


--
-- Name: common_paper_DOI_14ee925c_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "common_paper_DOI_14ee925c_like" ON public.common_paper USING btree ("DOI" varchar_pattern_ops);


--
-- Name: common_paper_publisher_id_a70e3e7b; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paper_publisher_id_a70e3e7b ON public.common_paper USING btree (publisher_id);


--
-- Name: common_paper_slug_0fcf4828_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paper_slug_0fcf4828_like ON public.common_paper USING btree (slug varchar_pattern_ops);


--
-- Name: common_paper_user_owner_id_ea0784cc; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paper_user_owner_id_ea0784cc ON public.common_paper USING btree (user_owner_id);


--
-- Name: common_paperauthor_author_id_2b56138f; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paperauthor_author_id_2b56138f ON public.common_paperauthor USING btree (author_id);


--
-- Name: common_paperauthor_paper_id_53f7190d; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paperauthor_paper_id_53f7190d ON public.common_paperauthor USING btree (paper_id);


--
-- Name: common_person_longName_613e60b4_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "common_person_longName_613e60b4_like" ON public.common_person USING btree ("longName" varchar_pattern_ops);


--
-- Name: common_person_org_id_fa830db5; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_person_org_id_fa830db5 ON public.common_person USING btree (org_id);


--
-- Name: common_person_shortName_7a8b3bab_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "common_person_shortName_7a8b3bab_like" ON public.common_person USING btree ("shortName" varchar_pattern_ops);


--
-- Name: dfndb_compositionpart_compound_id_98d443d4; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_compositionpart_compound_id_98d443d4 ON public.dfndb_compositionpart USING btree (compound_id);


--
-- Name: dfndb_compositionpart_material_id_c402ab5c; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_compositionpart_material_id_c402ab5c ON public.dfndb_compositionpart USING btree (material_id);


--
-- Name: dfndb_data_owner_id_35f0946e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_data_owner_id_35f0946e ON public.dfndb_data USING btree (user_owner_id);


--
-- Name: dfndb_data_paper_id_77124c38; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_data_paper_id_77124c38 ON public.dfndb_data USING btree (paper_id);


--
-- Name: dfndb_dataparameter_data_id_fd4b0c14; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_dataparameter_data_id_fd4b0c14 ON public.dfndb_dataparameter USING btree (data_id);


--
-- Name: dfndb_dataparameter_material_id_d751afed; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_dataparameter_material_id_d751afed ON public.dfndb_dataparameter USING btree (material_id);


--
-- Name: dfndb_dataparameter_parameter_id_90d736ce; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_dataparameter_parameter_id_90d736ce ON public.dfndb_dataparameter USING btree (parameter_id);


--
-- Name: dfndb_material_owner_id_d08667ca; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_material_owner_id_d08667ca ON public.dfndb_material USING btree (user_owner_id);


--
-- Name: dfndb_method_owner_id_a24ddb1e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_method_owner_id_a24ddb1e ON public.dfndb_method USING btree (user_owner_id);


--
-- Name: dfndb_parameter_owner_id_870086c2; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_parameter_owner_id_870086c2 ON public.dfndb_parameter USING btree (user_owner_id);


--
-- Name: dfndb_parameter_symbol_fd7c4ad6_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_parameter_symbol_fd7c4ad6_like ON public.dfndb_parameter USING btree (symbol varchar_pattern_ops);


--
-- Name: dfndb_parameter_unit_id_0d7cce7d; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_parameter_unit_id_0d7cce7d ON public.dfndb_parameter USING btree (unit_id);


--
-- Name: dfndb_quantityunit_name_62125fc1_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_quantityunit_name_62125fc1_like ON public.dfndb_quantityunit USING btree ("quantityName" varchar_pattern_ops);


--
-- Name: dfndb_quantityunit_related_unit_id_2a09ab35; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_quantityunit_related_unit_id_2a09ab35 ON public.dfndb_quantityunit USING btree (related_unit_id);


--
-- Name: dfndb_quantityunit_symbol_ae2875ca_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_quantityunit_symbol_ae2875ca_like ON public.dfndb_quantityunit USING btree ("quantitySymbol" varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_cellconfig battDB_cellconfig_user_owner_id_474eea19_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_cellconfig"
    ADD CONSTRAINT "battDB_cellconfig_user_owner_id_474eea19_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_datarange battDB_datarange_dataFile_id_ea79f7c6_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datarange"
    ADD CONSTRAINT "battDB_datarange_dataFile_id_ea79f7c6_fk_battDB_ex" FOREIGN KEY ("dataFile_id") REFERENCES public."battDB_experimentdatafile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_datarange battDB_datarange_user_owner_id_a458c111_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datarange"
    ADD CONSTRAINT "battDB_datarange_user_owner_id_a458c111_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicebatch battDB_devicebatch_device_type_id_f4cf37bf_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_device_type_id_f4cf37bf_fk_battDB_de" FOREIGN KEY (device_type_id) REFERENCES public."battDB_devicetype"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicebatch battDB_devicebatch_manufacturer_id_85675f1a_fk_common_org_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_manufacturer_id_85675f1a_fk_common_org_id" FOREIGN KEY (manufacturer_id) REFERENCES public.common_org(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicebatch battDB_devicebatch_user_owner_id_a17097e8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_user_owner_id_a17097e8_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceconfig battDB_deviceconfig_user_owner_id_9f82fb32_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfig"
    ADD CONSTRAINT "battDB_deviceconfig_user_owner_id_9f82fb32_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceconfignode battDB_deviceconfign_deviceConfig_id_5f8801f8_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfignode"
    ADD CONSTRAINT "battDB_deviceconfign_deviceConfig_id_5f8801f8_fk_battDB_de" FOREIGN KEY ("deviceConfig_id") REFERENCES public."battDB_deviceconfig"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceconfignode battDB_deviceconfign_deviceType_id_5184063c_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfignode"
    ADD CONSTRAINT "battDB_deviceconfign_deviceType_id_5184063c_fk_battDB_de" FOREIGN KEY ("deviceType_id") REFERENCES public."battDB_devicetype"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceconfignode battDB_deviceconfignode_user_owner_id_eebcdcc8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfignode"
    ADD CONSTRAINT "battDB_deviceconfignode_user_owner_id_eebcdcc8_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicetype battDB_devicetype_user_owner_id_e20a07ac_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicetype"
    ADD CONSTRAINT "battDB_devicetype_user_owner_id_e20a07ac_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipment battDB_equipment_type_id_92966c47_fk_battDB_equipmenttype_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_type_id_92966c47_fk_battDB_equipmenttype_id" FOREIGN KEY (type_id) REFERENCES public."battDB_equipmenttype"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipment battDB_equipment_user_owner_id_bbb9f49e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_user_owner_id_bbb9f49e_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipmenttype battDB_equipmenttype_user_owner_id_366e387f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipmenttype"
    ADD CONSTRAINT "battDB_equipmenttype_user_owner_id_366e387f_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment battDB_experiment_cellConfig_id_2d8d4638_fk_battDB_ce; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_cellConfig_id_2d8d4638_fk_battDB_ce" FOREIGN KEY ("cellConfig_id") REFERENCES public."battDB_cellconfig"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment battDB_experiment_protocol_id_ed0e9fcd_fk_dfndb_method_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_protocol_id_ed0e9fcd_fk_dfndb_method_id" FOREIGN KEY (protocol_id) REFERENCES public.dfndb_method(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment battDB_experiment_user_owner_id_3a1061fa_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_user_owner_id_3a1061fa_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdatafile battDB_experimentdat_experiment_id_de169b40_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdat_experiment_id_de169b40_fk_battDB_ex" FOREIGN KEY (experiment_id) REFERENCES public."battDB_experiment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdatafile battDB_experimentdat_machine_id_383367b5_fk_battDB_eq; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdat_machine_id_383367b5_fk_battDB_eq" FOREIGN KEY (machine_id) REFERENCES public."battDB_equipment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdatafile battDB_experimentdat_raw_data_file_id_91752398_fk_battDB_ra; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdat_raw_data_file_id_91752398_fk_battDB_ra" FOREIGN KEY (raw_data_file_id) REFERENCES public."battDB_rawdatafile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdatafile battDB_experimentdat_user_owner_id_f8f951f2_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdat_user_owner_id_f8f951f2_fk_auth_user" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_rawdatafile battDB_rawdatafile_user_owner_id_90ad71dd_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_rawdatafile"
    ADD CONSTRAINT "battDB_rawdatafile_user_owner_id_90ad71dd_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_basemodelwithslug common_basemodelwithslug_user_owner_id_b2ac42c9_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_basemodelwithslug
    ADD CONSTRAINT common_basemodelwithslug_user_owner_id_b2ac42c9_fk_auth_user_id FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_org common_org_manager_id_753c3111_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_org
    ADD CONSTRAINT common_org_manager_id_753c3111_fk_auth_user_id FOREIGN KEY (manager_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_paper common_paper_publisher_id_a70e3e7b_fk_common_org_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paper
    ADD CONSTRAINT common_paper_publisher_id_a70e3e7b_fk_common_org_id FOREIGN KEY (publisher_id) REFERENCES public.common_org(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_paper common_paper_user_owner_id_ea0784cc_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paper
    ADD CONSTRAINT common_paper_user_owner_id_ea0784cc_fk_auth_user_id FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_paperauthor common_paperauthor_author_id_2b56138f_fk_common_person_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paperauthor
    ADD CONSTRAINT common_paperauthor_author_id_2b56138f_fk_common_person_id FOREIGN KEY (author_id) REFERENCES public.common_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_paperauthor common_paperauthor_paper_id_53f7190d_fk_common_paper_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paperauthor
    ADD CONSTRAINT common_paperauthor_paper_id_53f7190d_fk_common_paper_id FOREIGN KEY (paper_id) REFERENCES public.common_paper(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_person common_person_org_id_fa830db5_fk_common_org_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person
    ADD CONSTRAINT common_person_org_id_fa830db5_fk_common_org_id FOREIGN KEY (org_id) REFERENCES public.common_org(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: common_person common_person_user_id_c5d7cec8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person
    ADD CONSTRAINT common_person_user_id_c5d7cec8_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_compositionpart dfndb_compositionpart_compound_id_98d443d4_fk_dfndb_compound_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compositionpart
    ADD CONSTRAINT dfndb_compositionpart_compound_id_98d443d4_fk_dfndb_compound_id FOREIGN KEY (compound_id) REFERENCES public.dfndb_compound(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_compositionpart dfndb_compositionpart_material_id_c402ab5c_fk_dfndb_material_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_compositionpart
    ADD CONSTRAINT dfndb_compositionpart_material_id_c402ab5c_fk_dfndb_material_id FOREIGN KEY (material_id) REFERENCES public.dfndb_material(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_data dfndb_data_paper_id_77124c38_fk_common_paper_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_data
    ADD CONSTRAINT dfndb_data_paper_id_77124c38_fk_common_paper_id FOREIGN KEY (paper_id) REFERENCES public.common_paper(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_data dfndb_data_user_owner_id_e6c8f500_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_data
    ADD CONSTRAINT dfndb_data_user_owner_id_e6c8f500_fk_auth_user_id FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_dataparameter dfndb_dataparameter_data_id_fd4b0c14_fk_dfndb_data_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_dataparameter
    ADD CONSTRAINT dfndb_dataparameter_data_id_fd4b0c14_fk_dfndb_data_id FOREIGN KEY (data_id) REFERENCES public.dfndb_data(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_dataparameter dfndb_dataparameter_material_id_d751afed_fk_dfndb_material_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_dataparameter
    ADD CONSTRAINT dfndb_dataparameter_material_id_d751afed_fk_dfndb_material_id FOREIGN KEY (material_id) REFERENCES public.dfndb_material(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_dataparameter dfndb_dataparameter_parameter_id_90d736ce_fk_dfndb_parameter_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_dataparameter
    ADD CONSTRAINT dfndb_dataparameter_parameter_id_90d736ce_fk_dfndb_parameter_id FOREIGN KEY (parameter_id) REFERENCES public.dfndb_parameter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_material dfndb_material_user_owner_id_a8f132d3_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_material
    ADD CONSTRAINT dfndb_material_user_owner_id_a8f132d3_fk_auth_user_id FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_method dfndb_method_user_owner_id_7e4e586f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_method
    ADD CONSTRAINT dfndb_method_user_owner_id_7e4e586f_fk_auth_user_id FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_parameter dfndb_parameter_unit_id_0d7cce7d_fk_dfndb_quantityunit_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_parameter
    ADD CONSTRAINT dfndb_parameter_unit_id_0d7cce7d_fk_dfndb_quantityunit_id FOREIGN KEY (unit_id) REFERENCES public.dfndb_quantityunit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_parameter dfndb_parameter_user_owner_id_18c94c30_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_parameter
    ADD CONSTRAINT dfndb_parameter_user_owner_id_18c94c30_fk_auth_user_id FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfndb_quantityunit dfndb_quantityunit_related_unit_id_2a09ab35_fk_dfndb_qua; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_quantityunit
    ADD CONSTRAINT dfndb_quantityunit_related_unit_id_2a09ab35_fk_dfndb_qua FOREIGN KEY (related_unit_id) REFERENCES public.dfndb_quantityunit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

