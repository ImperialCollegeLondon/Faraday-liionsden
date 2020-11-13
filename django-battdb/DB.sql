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
-- Name: battDB_batchdevice; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_batchdevice" (
    id integer NOT NULL,
    attributes jsonb NOT NULL,
    batch_id integer NOT NULL,
    seq_num smallint NOT NULL,
    notes text,
    CONSTRAINT "battDB_batchdevice_seq_num_check" CHECK ((seq_num >= 0))
);


ALTER TABLE public."battDB_batchdevice" OWNER TO towen;

--
-- Name: battDB_batchdevice_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_batchdevice_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_batchdevice_id_seq" OWNER TO towen;

--
-- Name: battDB_batchdevice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_batchdevice_id_seq" OWNED BY public."battDB_batchdevice".id;


--
-- Name: battDB_datacolumn; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_datacolumn" (
    id integer NOT NULL,
    column_name character varying(40) NOT NULL,
    resample character varying(10) NOT NULL,
    resample_n smallint NOT NULL,
    data_file_id integer NOT NULL,
    device_id integer,
    parameter_id integer,
    CONSTRAINT "battDB_datacolumn_resample_n_check" CHECK ((resample_n >= 0))
);


ALTER TABLE public."battDB_datacolumn" OWNER TO towen;

--
-- Name: battDB_datacolumn_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_datacolumn_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_datacolumn_id_seq" OWNER TO towen;

--
-- Name: battDB_datacolumn_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_datacolumn_id_seq" OWNED BY public."battDB_datacolumn".id;


--
-- Name: battDB_devicebatch; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_devicebatch" (
    id integer NOT NULL,
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(500) NOT NULL,
    "serialNo" character varying(60) NOT NULL,
    batch_size smallint NOT NULL,
    manufactured_on date NOT NULL,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    manufacturer_id integer,
    parent_id integer,
    specification_id integer,
    user_owner_id integer,
    manufacturing_protocol_id integer,
    inherit_metadata boolean NOT NULL,
    CONSTRAINT "battDB_devicebatch_batch_size_check" CHECK ((batch_size >= 0)),
    CONSTRAINT "battDB_devicebatch_level_check" CHECK ((level >= 0)),
    CONSTRAINT "battDB_devicebatch_lft_check" CHECK ((lft >= 0)),
    CONSTRAINT "battDB_devicebatch_rght_check" CHECK ((rght >= 0)),
    CONSTRAINT "battDB_devicebatch_status_check" CHECK ((status >= 0)),
    CONSTRAINT "battDB_devicebatch_tree_id_check" CHECK ((tree_id >= 0))
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
    slug character varying(500) NOT NULL,
    user_owner_id integer,
    config_type character varying(10) NOT NULL,
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
    device_position_id character varying(20),
    device_id integer NOT NULL,
    config_id integer NOT NULL,
    neg_netname character varying(20),
    pos_netname character varying(20)
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
-- Name: battDB_deviceparameter; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_deviceparameter" (
    id integer NOT NULL,
    name character varying(128),
    value jsonb,
    material_id integer,
    parameter_id integer NOT NULL,
    spec_id integer NOT NULL,
    inherit_to_children boolean NOT NULL
);


ALTER TABLE public."battDB_deviceparameter" OWNER TO towen;

--
-- Name: battDB_deviceparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_deviceparameter_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_deviceparameter_id_seq" OWNER TO towen;

--
-- Name: battDB_deviceparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_deviceparameter_id_seq" OWNED BY public."battDB_deviceparameter".id;


--
-- Name: battDB_devicespecification; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_devicespecification" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(500) NOT NULL,
    abstract boolean NOT NULL,
    complete boolean NOT NULL,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    device_type_id integer,
    parent_id integer,
    user_owner_id integer,
    inherit_metadata boolean NOT NULL,
    CONSTRAINT "battDB_devicespecification_level_check" CHECK ((level >= 0)),
    CONSTRAINT "battDB_devicespecification_lft_check" CHECK ((lft >= 0)),
    CONSTRAINT "battDB_devicespecification_rght_check" CHECK ((rght >= 0)),
    CONSTRAINT "battDB_devicespecification_status_check" CHECK ((status >= 0)),
    CONSTRAINT "battDB_devicespecification_tree_id_check" CHECK ((tree_id >= 0))
);


ALTER TABLE public."battDB_devicespecification" OWNER TO towen;

--
-- Name: battDB_devicespecification_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_devicespecification_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_devicespecification_id_seq" OWNER TO towen;

--
-- Name: battDB_devicespecification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_devicespecification_id_seq" OWNED BY public."battDB_devicespecification".id;


--
-- Name: battDB_equipment; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_equipment" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(500) NOT NULL,
    "serialNo" character varying(60) NOT NULL,
    manufacturer_id integer,
    specification_id integer,
    user_owner_id integer,
    default_parser_id integer,
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
-- Name: battDB_experiment; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_experiment" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(500) NOT NULL,
    date date NOT NULL,
    protocol_id integer,
    user_owner_id integer,
    config_id integer,
    folder_id integer,
    CONSTRAINT "battDB_experiment_status_check" CHECK ((status >= 0))
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
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(500) NOT NULL,
    raw_data_file_id integer,
    experiment_id integer,
    user_owner_id integer,
    parsed_metadata jsonb NOT NULL,
    machine_id integer,
    use_parser_id integer,
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
-- Name: battDB_experimentdevice; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_experimentdevice" (
    id integer NOT NULL,
    batch_seq smallint NOT NULL,
    device_pos character varying(20) NOT NULL,
    data_file_id integer,
    "deviceBatch_id" integer NOT NULL,
    experiment_id integer NOT NULL,
    CONSTRAINT "battDB_experimentdevice_batch_seq_1abc1dc2_check" CHECK ((batch_seq >= 0))
);


ALTER TABLE public."battDB_experimentdevice" OWNER TO towen;

--
-- Name: battDB_experimentdevice_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_experimentdevice_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_experimentdevice_id_seq" OWNER TO towen;

--
-- Name: battDB_experimentdevice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_experimentdevice_id_seq" OWNED BY public."battDB_experimentdevice".id;


--
-- Name: battDB_filefolder; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_filefolder" (
    id integer NOT NULL,
    name character varying(128),
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(500) NOT NULL,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    parent_id integer,
    user_owner_id integer,
    inherit_metadata boolean NOT NULL,
    CONSTRAINT "battDB_filefolder_level_check" CHECK ((level >= 0)),
    CONSTRAINT "battDB_filefolder_lft_check" CHECK ((lft >= 0)),
    CONSTRAINT "battDB_filefolder_rght_check" CHECK ((rght >= 0)),
    CONSTRAINT "battDB_filefolder_status_check" CHECK ((status >= 0)),
    CONSTRAINT "battDB_filefolder_tree_id_check" CHECK ((tree_id >= 0))
);


ALTER TABLE public."battDB_filefolder" OWNER TO towen;

--
-- Name: battDB_filefolder_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_filefolder_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_filefolder_id_seq" OWNER TO towen;

--
-- Name: battDB_filefolder_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_filefolder_id_seq" OWNED BY public."battDB_filefolder".id;


--
-- Name: battDB_harvester; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_harvester" (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    status smallint NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    attributes jsonb NOT NULL,
    notes text,
    slug character varying(500) NOT NULL,
    file_types character varying(20) NOT NULL,
    equipment_type_id integer,
    attach_to_experiment_id integer,
    user_owner_id integer,
    CONSTRAINT "battDB_harvester_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_harvester" OWNER TO towen;

--
-- Name: battDB_harvester_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_harvester_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_harvester_id_seq" OWNER TO towen;

--
-- Name: battDB_harvester_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_harvester_id_seq" OWNED BY public."battDB_harvester".id;


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
-- Name: battDB_parser; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_parser" (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    notes text,
    file_format character varying(20) NOT NULL,
    attributes jsonb NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    slug character varying(500) NOT NULL,
    status smallint NOT NULL,
    user_owner_id integer,
    CONSTRAINT "battDB_parser_status_check" CHECK ((status >= 0))
);


ALTER TABLE public."battDB_parser" OWNER TO towen;

--
-- Name: battDB_parser_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_parser_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_parser_id_seq" OWNER TO towen;

--
-- Name: battDB_parser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_parser_id_seq" OWNED BY public."battDB_parser".id;


--
-- Name: battDB_signaltype; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public."battDB_signaltype" (
    id integer NOT NULL,
    col_name character varying(50) NOT NULL,
    parameter_id integer NOT NULL,
    parser_id integer NOT NULL,
    "order" smallint NOT NULL,
    CONSTRAINT "battDB_signaltype_order_check" CHECK (("order" >= 0))
);


ALTER TABLE public."battDB_signaltype" OWNER TO towen;

--
-- Name: battDB_signaltype_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public."battDB_signaltype_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_signaltype_id_seq" OWNER TO towen;

--
-- Name: battDB_signaltype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public."battDB_signaltype_id_seq" OWNED BY public."battDB_signaltype".id;


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
    name character varying(128) NOT NULL,
    attributes jsonb NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    notes text,
    slug character varying(500) NOT NULL
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
    slug character varying(500) NOT NULL,
    authors character varying(300) NOT NULL,
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
-- Name: common_uploadedfile; Type: TABLE; Schema: public; Owner: towen
--

CREATE TABLE public.common_uploadedfile (
    id integer NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    file character varying(100) NOT NULL,
    hash character varying(64) NOT NULL,
    status smallint NOT NULL,
    user_owner_id integer,
    CONSTRAINT common_uploadedfile_status_check CHECK ((status >= 0))
);


ALTER TABLE public.common_uploadedfile OWNER TO towen;

--
-- Name: common_uploadedfile_id_seq; Type: SEQUENCE; Schema: public; Owner: towen
--

CREATE SEQUENCE public.common_uploadedfile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.common_uploadedfile_id_seq OWNER TO towen;

--
-- Name: common_uploadedfile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: towen
--

ALTER SEQUENCE public.common_uploadedfile_id_seq OWNED BY public.common_uploadedfile.id;


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
    mass double precision NOT NULL
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
    slug character varying(500) NOT NULL,
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
    slug character varying(500) NOT NULL,
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
    slug character varying(500) NOT NULL,
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
    slug character varying(500) NOT NULL,
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
-- Name: battDB_batchdevice id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_batchdevice" ALTER COLUMN id SET DEFAULT nextval('public."battDB_batchdevice_id_seq"'::regclass);


--
-- Name: battDB_datacolumn id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datacolumn" ALTER COLUMN id SET DEFAULT nextval('public."battDB_datacolumn_id_seq"'::regclass);


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
-- Name: battDB_deviceparameter id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceparameter" ALTER COLUMN id SET DEFAULT nextval('public."battDB_deviceparameter_id_seq"'::regclass);


--
-- Name: battDB_devicespecification id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicespecification" ALTER COLUMN id SET DEFAULT nextval('public."battDB_devicespecification_id_seq"'::regclass);


--
-- Name: battDB_equipment id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment" ALTER COLUMN id SET DEFAULT nextval('public."battDB_equipment_id_seq"'::regclass);


--
-- Name: battDB_experiment id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experiment_id_seq"'::regclass);


--
-- Name: battDB_experimentdatafile id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experimentdatafile_id_seq"'::regclass);


--
-- Name: battDB_experimentdevice id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdevice" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experimentdevice_id_seq"'::regclass);


--
-- Name: battDB_filefolder id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_filefolder" ALTER COLUMN id SET DEFAULT nextval('public."battDB_filefolder_id_seq"'::regclass);


--
-- Name: battDB_harvester id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_harvester" ALTER COLUMN id SET DEFAULT nextval('public."battDB_harvester_id_seq"'::regclass);


--
-- Name: battDB_parser id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_parser" ALTER COLUMN id SET DEFAULT nextval('public."battDB_parser_id_seq"'::regclass);


--
-- Name: battDB_signaltype id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_signaltype" ALTER COLUMN id SET DEFAULT nextval('public."battDB_signaltype_id_seq"'::regclass);


--
-- Name: common_org id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_org ALTER COLUMN id SET DEFAULT nextval('public.common_org_id_seq'::regclass);


--
-- Name: common_paper id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_paper ALTER COLUMN id SET DEFAULT nextval('public.common_paper_id_seq'::regclass);


--
-- Name: common_person id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_person ALTER COLUMN id SET DEFAULT nextval('public.common_person_id_seq'::regclass);


--
-- Name: common_uploadedfile id; Type: DEFAULT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_uploadedfile ALTER COLUMN id SET DEFAULT nextval('public.common_uploadedfile_id_seq'::regclass);


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
3	Equipment
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
29	1	29
30	1	30
31	1	31
32	1	32
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
97	2	29
98	2	30
99	2	31
100	2	32
113	2	128
114	2	129
115	2	130
116	2	131
117	2	132
118	2	136
119	2	137
120	2	138
121	2	139
122	2	140
123	2	144
124	2	149
125	2	150
126	2	151
127	2	152
128	2	192
129	2	197
130	2	198
131	2	199
132	2	200
133	2	201
134	2	202
135	2	203
136	2	204
137	2	85
138	2	86
139	2	87
140	2	88
141	2	89
142	2	90
143	2	91
144	2	92
145	2	120
146	2	225
147	2	226
148	2	227
149	2	228
150	2	105
151	2	108
152	2	237
153	2	238
154	2	239
155	2	240
156	2	112
157	2	124
158	2	244
159	2	245
160	2	246
161	2	247
162	2	248
163	2	249
164	2	116
165	2	117
166	2	252
167	2	118
168	2	125
169	3	89
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
253	Can add data parser	64	add_dataparser
254	Can change data parser	64	change_dataparser
255	Can delete data parser	64	delete_dataparser
256	Can view data parser	64	view_dataparser
29	Can add experiment	8	add_experiment
30	Can change experiment	8	change_experiment
31	Can delete experiment	8	delete_experiment
32	Can view experiment	8	view_experiment
257	Can add equipment	65	add_equipment
258	Can change equipment	65	change_equipment
259	Can delete equipment	65	delete_equipment
260	Can view equipment	65	view_equipment
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
269	Can add harvester	68	add_harvester
270	Can change harvester	68	change_harvester
271	Can delete harvester	68	delete_harvester
272	Can view harvester	68	view_harvester
85	Can add data range	22	add_datarange
86	Can change data range	22	change_datarange
87	Can delete data range	22	delete_datarange
88	Can view data range	22	view_datarange
89	Can add experiment data file	23	add_experimentdatafile
90	Can change experiment data file	23	change_experimentdatafile
91	Can delete experiment data file	23	delete_experimentdatafile
92	Can view experiment data file	23	view_experimentdatafile
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
261	Can add folder	66	add_folder
262	Can change folder	66	change_folder
263	Can delete folder	66	delete_folder
264	Can view folder	66	view_folder
149	Can add device batch	38	add_devicebatch
150	Can change device batch	38	change_devicebatch
151	Can delete device batch	38	delete_devicebatch
152	Can view device batch	38	view_devicebatch
273	Can add parser	69	add_parser
274	Can change parser	69	change_parser
275	Can delete parser	69	delete_parser
276	Can view parser	69	view_parser
277	Can add signal type	70	add_signaltype
278	Can change signal type	70	change_signaltype
279	Can delete signal type	70	delete_signaltype
280	Can view signal type	70	view_signaltype
177	Can add Token	45	add_token
178	Can change Token	45	change_token
179	Can delete Token	45	delete_token
180	Can view Token	45	view_token
181	Can add token	46	add_tokenproxy
182	Can change token	46	change_tokenproxy
183	Can delete token	46	delete_tokenproxy
184	Can view token	46	view_tokenproxy
189	Can add data parameter	48	add_dataparameter
190	Can change data parameter	48	change_dataparameter
191	Can delete data parameter	48	delete_dataparameter
192	Can view data parameter	48	view_dataparameter
197	Can add device config node	50	add_deviceconfignode
198	Can change device config node	50	change_deviceconfignode
199	Can delete device config node	50	delete_deviceconfignode
200	Can view device config node	50	view_deviceconfignode
201	Can add device config	51	add_deviceconfig
202	Can change device config	51	change_deviceconfig
203	Can delete device config	51	delete_deviceconfig
204	Can view device config	51	view_deviceconfig
225	Can add batch device	57	add_batchdevice
226	Can change batch device	57	change_batchdevice
227	Can delete batch device	57	delete_batchdevice
228	Can view batch device	57	view_batchdevice
237	Can add Data File to Device Mapping	60	add_datacolumn
238	Can change Data File to Device Mapping	60	change_datacolumn
239	Can delete Data File to Device Mapping	60	delete_datacolumn
240	Can view Data File to Device Mapping	60	view_datacolumn
241	Can add device specification	61	add_devicespecification
242	Can change device specification	61	change_devicespecification
243	Can delete device specification	61	delete_devicespecification
244	Can view device specification	61	view_devicespecification
245	Can add device parameter	62	add_deviceparameter
246	Can change device parameter	62	change_deviceparameter
247	Can delete device parameter	62	delete_deviceparameter
248	Can view device parameter	62	view_deviceparameter
249	Can add uploaded file	63	add_uploadedfile
250	Can change uploaded file	63	change_uploadedfile
251	Can delete uploaded file	63	delete_uploadedfile
252	Can view uploaded file	63	view_uploadedfile
265	Can add file folder	67	add_filefolder
266	Can change file folder	67	change_filefolder
267	Can delete file folder	67	delete_filefolder
268	Can view file folder	67	view_filefolder
281	Can add experiment device	71	add_experimentdevice
282	Can change experiment device	71	change_experimentdevice
283	Can delete experiment device	71	delete_experimentdevice
284	Can view experiment device	71	view_experimentdevice
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$150000$xjdfdhTwRhJ2$UXRtByrTwyL9b+c/+/4ttwBrsYYx4Z3gXbi7n7MqAyo=	\N	t	jacql	Jacqueline	Edge	j.edge@imperial.ac.uk	t	t	2020-08-11 11:11:31+01
3	pbkdf2_sha256$150000$EfLnuKoVFTo5$eI9zlUW09YuBiHiPdlpYqbf8cFyvRvTISVec8IqZaUw=	2020-08-13 10:56:28+01	t	binbin	Binbin	Chen		t	t	2020-08-13 09:53:36+01
7	pbkdf2_sha256$216000$Vt9WFAxpjSyE$nW6zcHd0uYfDqElZJ+RkFpcN3t9RDAPKyWGARyQdUw4=	2020-10-08 13:36:25.920895+01	f	test	Test	User		t	t	2020-10-08 13:33:36+01
8	pbkdf2_sha256$216000$rtzqcHSiEh62$Dzt8NBZjs+1qEmcZRFNHE3c1pMi7CAFMMRK04c52UWg=	\N	f	cycler-foobar5000				f	t	2020-11-04 11:59:55+00
1	pbkdf2_sha256$216000$OafoLVPyzITM$orFVUO5QzVoBneWLEpu4jxz+Ucrc+DqclzTFOsJcvH4=	2020-11-10 12:05:26.628986+00	t	tom	Tom	Owen	tom.owen@zepler.net	t	t	2020-08-04 19:08:06+01
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
1	3	2
2	8	3
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
29	2	29
30	2	30
31	2	31
32	2	32
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
69	7	128
71	7	132
73	7	136
75	7	140
77	7	144
81	7	32
83	7	40
84	7	44
85	7	48
86	7	52
87	7	56
88	7	60
95	7	88
96	7	92
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
c2fdceacffa198fd09d3f5baa7821b14f0ce0f22	2020-11-04 12:41:17.743212+00	8
\.


--
-- Data for Name: battDB_batchdevice; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_batchdevice" (id, attributes, batch_id, seq_num, notes) FROM stdin;
2	{}	32	1	\N
3	{}	32	2	\N
5	{}	32	4	
6	{"state_of_health": "100%"}	32	5	foo
4	{"state_of_health": "100%"}	32	3	.
8	{}	32	0	\N
\.


--
-- Data for Name: battDB_datacolumn; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_datacolumn" (id, column_name, resample, resample_n, data_file_id, device_id, parameter_id) FROM stdin;
\.


--
-- Data for Name: battDB_devicebatch; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_devicebatch" (id, status, created_on, modified_on, attributes, notes, slug, "serialNo", batch_size, manufactured_on, lft, rght, tree_id, level, manufacturer_id, parent_id, specification_id, user_owner_id, manufacturing_protocol_id, inherit_metadata) FROM stdin;
32	10	2020-11-01 17:41:49.156174+00	2020-11-12 16:50:19.715247+00	{}		imperial-college-my-nmc622-cell-5-off-2020-11-01	B%d	5	2020-11-01	1	2	1	0	1	\N	7	1	\N	t
\.


--
-- Data for Name: battDB_deviceconfig; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_deviceconfig" (id, name, status, created_on, modified_on, attributes, notes, slug, user_owner_id, config_type) FROM stdin;
4	2s2p module	10	2020-11-02 12:35:00.339675+00	2020-11-02 12:56:54.504165+00	{}		2s2p-module	1	module
\.


--
-- Data for Name: battDB_deviceconfignode; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_deviceconfignode" (id, device_position_id, device_id, config_id, neg_netname, pos_netname) FROM stdin;
9	A1	6	4	V0	V1
10	A2	6	4	V0	V1
11	B1	6	4	V1	V2
12	B2	6	4	V1	V2
14	+	17	4	\N	V2
15	-	17	4	\N	V0
16	T	17	4	\N	V1
\.


--
-- Data for Name: battDB_deviceparameter; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_deviceparameter" (id, name, value, material_id, parameter_id, spec_id, inherit_to_children) FROM stdin;
1	Pack capacity	\N	\N	3	4	f
2	Module capacity	\N	\N	3	5	f
3	Cell Capacity	\N	\N	3	6	f
4	Electrode Thickness	1	1	2	21	f
\.


--
-- Data for Name: battDB_devicespecification; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_devicespecification" (id, name, status, created_on, modified_on, attributes, notes, slug, abstract, complete, lft, rght, tree_id, level, device_type_id, parent_id, user_owner_id, inherit_metadata) FROM stdin;
9	Positive Electrode	10	2020-11-02 12:16:18.676514+00	2020-11-02 12:18:39.030117+00	{}		positive-electrode	t	f	4	7	1	3	\N	6	\N	t
5	Module	10	2020-11-01 17:25:16.061485+00	2020-11-12 21:24:48.552232+00	{}		module	t	t	2	23	1	1	\N	4	\N	f
4	Pack	10	2020-11-01 17:25:16.059603+00	2020-11-12 21:25:13.933661+00	{}		pack	t	t	1	26	1	0	\N	\N	1	t
10	Negative Electrode	10	2020-11-02 12:16:18.677955+00	2020-11-02 12:19:21.467412+00	{}		negative-electrode	t	f	8	11	1	3	\N	6	\N	t
14	Neg. E'trode Material	10	2020-11-02 12:19:21.469428+00	2020-11-02 12:19:21.469438+00	{}		neg-etrode-material	t	f	9	10	1	4	\N	10	\N	t
13	Pos. E'trode Material	10	2020-11-02 12:18:39.032358+00	2020-11-02 12:19:46.361764+00	{}		pos-etrode-material	t	f	5	6	1	4	\N	9	\N	t
12	Electrolyte	10	2020-11-02 12:16:18.680618+00	2020-11-02 12:16:18.680627+00	{}		electrolyte	t	f	16	17	1	3	\N	6	\N	t
11	Separator	10	2020-11-02 12:16:18.679339+00	2020-11-02 12:20:17.379271+00	{}		separator	t	f	12	15	1	3	\N	6	\N	t
15	Separator Material	10	2020-11-02 12:20:17.381227+00	2020-11-02 12:20:17.381239+00	{}		separator-material	t	f	13	14	1	4	\N	11	\N	t
16	Cell Casing	10	2020-11-02 12:20:56.097147+00	2020-11-02 12:20:56.097157+00	{}		cell-casing	t	f	18	19	1	3	\N	6	\N	t
6	Cell	10	2020-11-01 17:27:16.425737+00	2020-11-02 12:42:33.456044+00	{}		cell	t	t	3	20	1	2	\N	5	1	t
17	Terminal	10	2020-11-02 12:52:36.100321+00	2020-11-02 12:52:36.100332+00	{}		terminal	t	f	21	22	1	2	\N	5	\N	t
18	Connector	10	2020-11-02 12:52:59.707199+00	2020-11-02 13:01:53.108119+00	{}		connector	t	f	24	25	1	1	\N	4	\N	t
19	Cycler Machine	10	2020-11-04 12:38:04.208567+00	2020-11-04 12:38:04.208583+00	{}		cycler-machine	t	f	1	2	4	0	\N	\N	1	t
8	My NMC622 Module	10	2020-11-01 17:45:04.963155+00	2020-11-01 17:45:33.655848+00	{}		my-nmc622-module	f	t	1	8	3	0	5	\N	1	t
21	Positive Electrode Material	10	2020-11-12 16:56:28.553483+00	2020-11-12 18:01:07.031781+00	{}		positive-electrode-material	f	f	5	6	3	2	13	7	1	t
7	My NMC622 Cell	10	2020-11-01 17:36:29.295484+00	2020-11-12 18:01:12.853761+00	{}		my-nmc622-cell	f	t	4	7	3	1	6	8	1	t
\.


--
-- Data for Name: battDB_equipment; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_equipment" (id, name, status, created_on, modified_on, attributes, notes, slug, "serialNo", manufacturer_id, specification_id, user_owner_id, default_parser_id) FROM stdin;
1	GalvoTron 5000	10	2020-11-04 12:39:37.006194+00	2020-11-04 12:39:37.006214+00	{}		galvotron-5000		1	\N	1	\N
\.


--
-- Data for Name: battDB_experiment; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_experiment" (id, name, status, created_on, modified_on, attributes, notes, slug, date, protocol_id, user_owner_id, config_id, folder_id) FROM stdin;
7	\N	10	2020-11-10 13:01:21.234456+00	2020-11-10 13:01:21.234488+00	{}	\N	none-none-2020-11-10-130121233994	2020-11-10	\N	\N	\N	\N
8	fo	10	2020-11-10 13:02:30.124113+00	2020-11-10 13:02:30.124164+00	{}	\N	none-fo-2020-11-10-130230123371	2020-11-10	\N	\N	\N	\N
6	\N	10	2020-11-10 12:56:33.537583+00	2020-11-11 19:35:54.923375+00	{}		tom-none-2020-11-10	2020-11-10	\N	1	\N	\N
5	My experiment	10	2020-11-01 17:43:36.325635+00	2020-11-12 15:09:24.691614+00	{}		tom-my-experiment-2020-11-01	2020-11-01	4	1	\N	\N
\.


--
-- Data for Name: battDB_experimentdatafile; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_experimentdatafile" (id, status, created_on, modified_on, attributes, notes, slug, raw_data_file_id, experiment_id, user_owner_id, parsed_metadata, machine_id, use_parser_id) FROM stdin;
16	10	2020-11-02 17:02:54.67311+00	2020-11-05 15:55:49.316338+00	{}		mugjpeg	17	\N	1	{"columns": {}}	\N	\N
18	10	2020-11-05 15:33:41.286298+00	2020-11-13 16:36:40.906773+00	{"file_rows": 1168866, "file_columns": ["mode", "ox/red", "error", "control changes", "Ns changes", "counter inc", "Ns", "I Range", "Time", "control/V/mA", "Ecell/V", "I/mA", "dq/mA_h", "(Q-Qo)/mA_h", "Energy/W_h", "Energy charge/W_h", "Energy discharge/W_h", "Capacitance charge/�F", "Capacitance discharge/�F", "x", "Q discharge/mA_h", "Q charge/mA_h", "Capacity/mA_h", "Efficiency/%", "control/V", "control/mA", "cycle number", "P/W", "R/Ohm", "Rec#"], "range_config": {"all": {"end": 1168866, "start": 1, "action": "all"}}, "parsed_ranges": {"all": {"end": 1168866, "start": 1, "action": "all"}}, "parsed_columns": ["Ecell/V", "I/mA", "control/V"], "missing_columns": []}		c_over_20_run_25_c_ca1txt	22	\N	1	{"num_rows": 1168866, "warnings": [], "data_start": 84, "file_header": ["BT-Lab ASCII FILE\\n", "Nb header lines : 85                          \\n", "\\n", "Modulo Bat\\n", "\\n", "Run on channel : A1 (SN 0322)\\n", "Grouped channel(s) : A1, A2, A3, A4, A5\\n", "User : \\n", "Ecell ctrl range : min = 0.00 V, max = 9.00 V\\n", "Safety Limits :\\n", "\\tEcell min = 2.45 V\\n", "\\tEcell max = 4.25 V\\n", "\\tfor t > 10 ms\\n", "Acquisition started on : 11/11/2019 12:25:53\\n", "Saved on :\\n", "\\tFile : C over 20 run 25 °C_CA1.mpr\\n", "\\tDirectory : D:\\\\Data\\\\Karthik\\\\MSM - AGM Single layer\\\\5 Cell Referenece tests\\\\Matrix  Tests\\\\25 ° Characterization\\\\C over 20\\\\\\n", "\\tHost : 192.109.209.129\\n", "Device : BCS-815 (SN 0455)\\n", "Address : 192.109.209.128\\n", "BT-Lab for windows v1.65 (software)\\n", "Internet server v1.65 (firmware)\\n", "Command interpretor v1.65 (firmware)\\n", "Electrode material : \\n", "Initial state : \\n", "Electrolyte : \\n", "Comments : \\n", "Mass of active material : 0.001 mg\\n", " at x = 0.000\\n", "Molecular weight of active material (at x = 0) : 0.001 g/mol\\n", "Atomic weight of intercalated ion : 0.001 g/mol\\n", "Acquisition started at : xo = 0.000\\n", "Number of e- transfered per intercalated ion : 1\\n", "for DX = 1, DQ = 26.802 mA.h\\n", "Battery capacity : 1.000 A.h\\n", "Electrode surface area : 0.001 cm²\\n", "Characteristic mass : 0.001 g\\n", "Cycle Definition : Charge/Discharge alternance\\n", "Ns                  0                   1                   2                   3                   4                   5                   6                   7                   8                   \\n", "ctrl_type           Rest                CC                  CV                  Rest                CC                  CV                  Rest                Loop                Rest                \\n", "Apply I/C           I                   I                   I                   I                   I                   I                   I                   I                   I                   \\n", "ctrl1_val                               13.000              4.200                                   13.000              2.500                                   15.000                                  \\n", "ctrl1_val_unit                          mA                  V                                       mA                  V                                                                               \\n", "ctrl1_val_vs                            <None>              Ref                                     <None>              Ref                                                                             \\n", "ctrl2_val                                                                                                                                                                                               \\n", "ctrl2_val_unit                                                                                                                                                                                          \\n", "ctrl2_val_vs                                                                                                                                                                                            \\n", "ctrl3_val                                                                                                                                                                                               \\n", "ctrl3_val_unit                                                                                                                                                                                          \\n", "ctrl3_val_vs                                                                                                                                                                                            \\n", "N                   1.00                1.00                1.00                1.00                1.00                1.00                1.00                1.00                1.00                \\n", "charge/discharge    Charge              Charge              Charge              Charge              Discharge           Discharge           Discharge           Discharge           Discharge           \\n", "ctrl_seq            0                   0                   0                   0                   0                   0                   0                   1                   1                   \\n", "ctrl_repeat         0                   0                   0                   0                   0                   0                   0                   4                   4                   \\n", "ctrl_trigger        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        \\n", "ctrl_TO_t           0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "ctrl_TO_t_unit      d                   d                   d                   d                   d                   d                   d                   d                   d                   \\n", "ctrl_Nd             6                   6                   6                   6                   6                   6                   6                   6                   6                   \\n", "ctrl_Na             1                   1                   1                   1                   1                   1                   1                   1                   1                   \\n", "ctrl_corr           1                   1                   1                   1                   1                   1                   1                   1                   1                   \\n", "lim_nb              1                   1                   1                   1                   1                   1                   1                   0                   1                   \\n", "lim1_type           Time                Ecell               |I|                 Time                Ecell               |I|                 Time                Ecell               Time                \\n", "lim1_comp           >                   >                   <                   >                   <                   <                   >                   <                   >                   \\n", "lim1_Q              Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             \\n", "lim1_value          5.000               4.200               5.000               2.000               2.500               5.000               2.000               2.500               2.000               \\n", "lim1_value_unit     s                   V                   mA                  h                   V                   mA                  h                   V                   h                   \\n", "lim1_action         Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       \\n", "lim1_seq            1                   2                   3                   4                   5                   6                   7                   8                   9                   \\n", "rec_nb              1                   2                   2                   1                   2                   2                   1                   0                   1                   \\n", "rec1_type           Time                Time                Time                Time                Time                Time                Time                Time                Time                \\n", "rec1_value          1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               \\n", "rec1_value_unit     mn                  s                   s                   s                   s                   s                   s                   s                   s                   \\n", "rec2_type           Time                Ecell               I                   Time                Ecell               I                   I                   Time                Time                \\n", "rec2_value          0.000               10.000              0.150               0.000               10.000              0.150               1.000               0.000               0.000               \\n", "rec2_value_unit     s                   mV                  mA                  s                   mV                  mA                  mA                  s                   s                   \\n", "E range min (V)     0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "E range max (V)     9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               \\n", "I Range             10 mA               10 mA               Auto                1 A                 10 mA               Auto                100 mA              10 mA               1 A                 \\n", "I Range min         Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "I Range max         Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "I Range init        Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "auto rest           0                   0                   0                   0                   0                   0                   0                   0                   0                   \\n", "Bandwidth           4                   4                   4                   4                   4                   4                   4                   4                   4                   \\n", "\\n"], "Dataset_Name": "C_over_20_run_25_C_CA1", "dataset_size": 517385203, "Device Metadata": {"Mode": "Modulo Bat", "User": null, "DX/DQ": "for DX = 1, DQ = 26.802 mA.h", "Device": "BCS-815 (SN 0455)", "Address": "192.109.209.128", "Comments": null, "FileType": "BT-Lab ASCII FILE", "Saved on": {"File": "C over 20 run 25 °C_CA1.mpr", "Host": "192.109.209.129", "Directory": "D:\\\\Data\\\\Karthik\\\\MSM - AGM Single layer\\\\5 Cell Referenece tests\\\\Matrix  Tests\\\\25 ° Characterization\\\\C over 20\\\\"}, "Electrolyte": null, "Initial state": null, "Safety Limits": "Ecell min = 2.45 V Ecell max = 4.25 V for t > 10 ms", "Run on channel": "A1 (SN 0322)", "Internet server": "v1.65 (firmware)", "Nb header lines": 85, "Battery capacity": "1.000 A.h", "Cycle Definition": "Charge/Discharge alternance", "Ecell ctrl range": "min = 0.00 V, max = 9.00 V", "BT-Lab for windows": "v1.65 (software)", "Electrode material": null, "Grouped channel(s)": "A1, A2, A3, A4, A5", "Characteristic mass": "0.001 g", "Command interpretor": "v1.65 (firmware)", "Acquisition started at": "xo = 0.000", "Acquisition started on": "11/11/2019 12:25:53", "Electrode surface area": "0.001 cm²", "Mass of active material": "0.001 mg at x = 0.000", "Atomic weight of intercalated ion": "0.001 g/mol", "Number of e- transfered per intercalated ion": 1, "Molecular weight of active material (at x = 0)": "0.001 g/mol"}, "first_sample_no": 85}	\N	1
17	10	2020-11-02 18:07:10.755531+00	2020-11-13 16:12:13.735118+00	{"file_rows": 149, "file_columns": ["mode", "ox/red", "error", "control changes", "Ns changes", "counter inc", "Ns", "I Range", "Time", "control/V/mA", "Ecell/V", "I/mA", "dq/mA_h", "(Q-Qo)/mA_h", "Energy/W_h", "Analog IN 1/V", "Analog OUT/V", "Energy charge/W_h", "Energy discharge/W_h", "Capacitance charge/�F", "Capacitance discharge/�F", "x", "Q discharge/mA_h", "Q charge/mA_h", "Capacity/mA_h", "Efficiency/%", "control/V", "control/mA", "cycle number", "P/W", "R/Ohm", "Rec#"], "range_config": {"all": {"end": 149, "start": 1, "action": "all"}}, "parsed_ranges": {"all": {"end": 149, "start": 1, "action": "all"}}, "parsed_columns": ["Time", "Ecell/V", "I/mA", "control/V"], "missing_columns": []}		biologic_fulltxt	18	5	1	{"num_rows": 149, "warnings": [], "data_start": 101, "file_header": ["BT-Lab ASCII FILE\\n", "Nb header lines : 102                         \\n", "\\n", "Modulo Bat\\n", "\\n", "Run on channel : E1 (SN 0355)\\n", "User : \\n", "Ecell ctrl range : min = 0.00 V, max = 9.00 V\\n", "Safety Limits :\\n", "\\tEcell min = 2.50 V\\n", "\\tEcell max = 4.35 V\\n", "\\tfor t > 10 ms\\n", "Acquisition started on : 08/19/2019 16:31:18\\n", "Saved on :\\n", "\\tFile : Cathode_CE1.mpr\\n", "\\tDirectory : D:\\\\Data\\\\Ryan\\\\Entropy CoinCells 18Aug\\\\\\n", "\\tHost : 192.109.209.129\\n", "Device : BCS-815 (SN 0455)\\n", "Address : 192.109.209.128\\n", "BT-Lab for windows v1.65 (software)\\n", "Internet server v1.65 (firmware)\\n", "Command interpretor v1.65 (firmware)\\n", "Electrode material : \\n", "Initial state : \\n", "Electrolyte : \\n", "Comments : \\n", "Mass of active material : 0.001 mg\\n", " at x = 0.000\\n", "Molecular weight of active material (at x = 0) : 0.001 g/mol\\n", "Atomic weight of intercalated ion : 0.001 g/mol\\n", "Acquisition started at : xo = 0.000\\n", "Number of e- transfered per intercalated ion : 1\\n", "for DX = 1, DQ = 26.802 mA.h\\n", "Battery capacity : 2.230 mA.h\\n", "Electrode surface area : 0.001 cm²\\n", "Characteristic mass : 0.001 g\\n", "Record Analogic IN 1\\n", "Cycle Definition : Charge/Discharge alternance\\n", "External device configuration :\\n", "   device type : Other\\n", "   device name : Other\\n", "   Analog OUT : \\n", "      mode : E/V\\n", "      unit : E/V\\n", "      max : 5.000 at 5.000 V\\n", "      min : 0.000 at 0.000 V\\n", "      current : 0.000\\n", "   Analog IN 1 : \\n", "      unit : E/V\\n", "      max : 5.000 at 5.000 V\\n", "      min : 0.000 at 0.000 V\\n", "Ns                  0                   1                   2                   3                   4                   5                   6                   7                   8                   9                   10                  11                  12                  13                  14                  15                  16                  17                  18                  19                  20                  21                  22                  23                  24                  25                  26                  27                  28                  29                  \\n", "ctrl_type           Rest                Rest                CC                  CV                  Rest                TO                  Rest                Rest                Rest                Rest                Rest                Rest                CC                  Rest                TO                  Rest                Rest                Rest                Rest                Rest                Rest                Loop                CV                  TO                  Rest                Rest                Rest                Rest                Rest                Rest                \\n", "Apply I/C           I                   I                   C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               \\n", "ctrl1_val                                                   0.000               4.300                                   2.700                                                                                                                                       100.000                                 100.000                                                                                                                                     100.000             2.700               4.300                                                                                                                                       \\n", "ctrl1_val_unit                                              mA                  V                                                                                                                                                                                   mA                                                                                                                                                                                                      V                                                                                                                                                               \\n", "ctrl1_val_vs                                                <None>              Ref                                                                                                                                                                                 <None>                                                                                                                                                                                                  Ref                                                                                                                                                             \\n", "ctrl2_val                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   \\n", "ctrl2_val_unit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              \\n", "ctrl2_val_vs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                \\n", "ctrl3_val                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   \\n", "ctrl3_val_unit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              \\n", "ctrl3_val_vs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                \\n", "N                   1.00                1.00                1.00                3.00                3.00                3.00                3.00                3.00                3.00                3.00                3.00                3.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                \\n", "charge/discharge    Charge              Charge              Charge              Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              \\n", "ctrl_seq            0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   12                  12                  12                  0                   0                   0                   0                   0                   0                   \\n", "ctrl_repeat         0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   60                  60                  60                  0                   0                   0                   0                   0                   0                   \\n", "ctrl_trigger        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Rising Edge         Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Rising Edge         Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Rising Edge         Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        \\n", "ctrl_TO_t           0.000               0.000               0.000               0.000               0.000               2.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               2.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               2.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "ctrl_TO_t_unit      d                   d                   d                   d                   d                   s                   d                   d                   d                   d                   d                   d                   d                   d                   s                   d                   d                   d                   d                   d                   d                   d                   d                   s                   d                   d                   d                   d                   d                   d                   \\n", "ctrl_Nd             6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   \\n", "ctrl_Na             1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   \\n", "ctrl_corr           1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   \\n", "lim_nb              1                   1                   1                   1                   1                   0                   1                   1                   1                   1                   1                   1                   2                   1                   0                   1                   1                   1                   1                   1                   1                   0                   1                   0                   1                   1                   1                   1                   1                   1                   \\n", "lim1_type           Time                Time                Time                Ecell               |I|                 Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                |I|                 \\n", "lim1_comp           >                   >                   >                   <                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   <                   <                   >                   >                   >                   >                   >                   >                   \\n", "lim1_Q              Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             \\n", "lim1_value          3.000               3.000               4.300               23.000              90.000              90.000              3.000               3.000               3.000               3.000               3.000               10.000              6.000               90.000              90.000              3.000               3.000               3.000               3.000               3.000               10.000              10.000              23.000              23.000              3.000               3.000               3.000               3.000               3.000               10.000              \\n", "lim1_value_unit     d                   s                   s                   V                   mA                  mn                  d                   s                   d                   s                   d                   mn                  mn                  mn                  mn                  d                   s                   d                   s                   d                   mn                  mn                  s                   s                   d                   s                   d                   s                   d                   mA                  \\n", "lim1_action         Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       \\n", "lim1_seq            1                   2                   3                   4                   5                   6                   7                   8                   9                   10                  11                  12                  13                  14                  15                  16                  17                  18                  19                  20                  21                  22                  23                  24                  25                  26                  27                  28                  29                  30                  \\n", "lim2_type           Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Ecell               Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                \\n", "lim2_comp           <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   \\n", "lim2_Q              Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             \\n", "lim2_value          0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               2.700               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "lim2_value_unit     s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   V                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   \\n", "lim2_action         Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Goto sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       \\n", "lim2_seq            1                   2                   3                   4                   5                   6                   7                   8                   9                   10                  11                  12                  22                  14                  15                  16                  17                  18                  19                  20                  21                  22                  23                  24                  25                  26                  27                  28                  29                  30                  \\n", "rec_nb              0                   0                   1                   1                   1                   0                   1                   1                   1                   1                   1                   1                   1                   1                   0                   1                   1                   1                   1                   1                   1                   0                   1                   0                   1                   1                   1                   1                   1                   1                   \\n", "rec1_type           Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                \\n", "rec1_value          1.000               1.000               1.000               1.000               10.000              10.000              1.000               1.000               1.000               1.000               1.000               1.000               1.000               10.000              10.000              1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               \\n", "rec1_value_unit     s                   s                   s                   mn                  s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   \\n", "E range min (V)     0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "E range max (V)     9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               \\n", "I Range             10 mA               10 mA               1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                \\n", "I Range min         Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "I Range max         Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "I Range init        Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "auto rest           0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   \\n", "Bandwidth           4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   \\n", "\\n"], "Dataset_Name": "BioLogic_full", "dataset_size": 101861, "Device Metadata": {"Mode": "Modulo Bat", "User": null, "DX/DQ": "for DX = 1, DQ = 26.802 mA.h", "Device": "BCS-815 (SN 0455)", "Record": "Analogic IN 1", "Address": "192.109.209.128", "Comments": null, "FileType": "BT-Lab ASCII FILE", "Saved on": {"File": "Cathode_CE1.mpr", "Host": "192.109.209.129", "Directory": "D:\\\\Data\\\\Ryan\\\\Entropy CoinCells 18Aug\\\\"}, "Electrolyte": null, "Initial state": null, "Safety Limits": "Ecell min = 2.50 V Ecell max = 4.35 V for t > 10 ms", "Run on channel": "E1 (SN 0355)", "Internet server": "v1.65 (firmware)", "Nb header lines": 102, "Battery capacity": "2.230 mA.h", "Cycle Definition": "Charge/Discharge alternance", "Ecell ctrl range": "min = 0.00 V, max = 9.00 V", "BT-Lab for windows": "v1.65 (software)", "Electrode material": null, "Characteristic mass": "0.001 g", "Command interpretor": "v1.65 (firmware)", "Acquisition started at": "xo = 0.000", "Acquisition started on": "08/19/2019 16:31:18", "Electrode surface area": "0.001 cm²", "Mass of active material": "0.001 mg at x = 0.000", "External device configuration": {"Analog OUT": {"max": "5.000 at 5.000 V", "min": "0.000 at 0.000 V", "mode": "E/V", "unit": "E/V", "current": 0.0}, "Analog IN 1": {"max": "5.000 at 5.000 V", "min": "0.000 at 0.000 V", "unit": "E/V"}, "device name": "Other", "device type": "Other"}, "Atomic weight of intercalated ion": "0.001 g/mol", "Number of e- transfered per intercalated ion": 1, "Molecular weight of active material (at x = 0)": "0.001 g/mol"}, "first_sample_no": 102}	\N	2
\.


--
-- Data for Name: battDB_experimentdevice; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_experimentdevice" (id, batch_seq, device_pos, data_file_id, "deviceBatch_id", experiment_id) FROM stdin;
1	0	cell_nn	17	32	5
3	1	cell_nn1	17	32	5
\.


--
-- Data for Name: battDB_filefolder; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_filefolder" (id, name, status, created_on, modified_on, attributes, notes, slug, lft, rght, tree_id, level, parent_id, user_owner_id, inherit_metadata) FROM stdin;
1	My Folder	10	2020-11-04 09:38:43.228605+00	2020-11-04 09:38:43.228628+00	{}		my-folder	1	4	1	0	\N	1	t
2	Another Folder	10	2020-11-04 09:38:58.362381+00	2020-11-04 09:38:58.362395+00	{}		another-folder	2	3	1	1	1	1	t
\.


--
-- Data for Name: battDB_harvester; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_harvester" (id, name, status, created_on, modified_on, attributes, notes, slug, file_types, equipment_type_id, attach_to_experiment_id, user_owner_id) FROM stdin;
1	makron	10	2020-11-04 12:40:28.873201+00	2020-11-11 19:15:53.425912+00	{}		makron	*.csv	1	5	1
2	foo	10	2020-11-11 19:35:39.944867+00	2020-11-11 19:35:39.944882+00	{}		foo	*.csv	\N	\N	1
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
-- Data for Name: battDB_parser; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_parser" (id, name, notes, file_format, attributes, created_on, modified_on, slug, status, user_owner_id) FROM stdin;
2	Biologix Default		biologic	{}	2020-11-13 16:10:41.670367+00	2020-11-13 16:10:41.670384+00	biologix-default	10	1
1	Biologix V,I,CV		biologic	{}	2020-11-10 15:18:25.987275+00	2020-11-13 16:11:03.188506+00	biologix-vicv	10	1
\.


--
-- Data for Name: battDB_signaltype; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public."battDB_signaltype" (id, col_name, parameter_id, parser_id, "order") FROM stdin;
1	Ecell/V	4	1	1
2	I/mA	7	1	1
3	control/V	10	1	1
5	Time	11	2	0
6	Ecell/V	4	2	1
7	I/mA	7	2	1
8	control/V	10	2	1
\.


--
-- Data for Name: common_org; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_org (id, website, is_mfg_cells, is_mfg_equip, is_publisher, is_research, manager_id, name, attributes, created_on, modified_on, notes, slug) FROM stdin;
1	http://imperial.ac.uk	t	f	f	t	\N	Imperial College	{}	2020-10-21 12:38:47.020706+01	2020-10-21 12:38:47.033474+01	\N	autogenerated
2	\N	f	f	f	f	\N	Bob's company	{}	2020-10-21 12:38:47.020706+01	2020-10-21 12:38:47.033474+01	\N	autogenerated
\.


--
-- Data for Name: common_paper; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_paper (id, "DOI", year, title, url, publisher_id, attributes, status, user_owner_id, notes, "PDF", modified_on, created_on, slug, authors) FROM stdin;
1	https://doi.org/10.1109/5.771073	2019	Toward unique identifiers	https://ieeexplore.ieee.org/document/771073	\N	{}	10	\N	.		2020-10-19 16:59:28.034498+01	2020-10-15 18:18:05.103148+01	toward-unique-identifiers-2019	
\.


--
-- Data for Name: common_person; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_person (id, org_id, user_id, "longName", "shortName") FROM stdin;
1	1	1	Tom Owen	T.Owen
2	\N	\N	nobby	n
\.


--
-- Data for Name: common_uploadedfile; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.common_uploadedfile (id, created_on, modified_on, file, hash, status, user_owner_id) FROM stdin;
17	2020-11-01 18:20:38.799315+00	2020-11-01 18:20:38.806274+00	uploaded_files/mug.jpeg	f5009ba783fd94b0a410738e13dafa14	10	\N
18	2020-11-02 10:59:35.647447+00	2020-11-02 10:59:35.647505+00	uploaded_files/BioLogic_full.txt	abf6e42283668f8ba9094a0f85411f64	10	\N
19	2020-11-02 14:40:08.578715+00	2020-11-02 14:40:08.578729+00	uploaded_files/Ivium_Cell1.txt	b35947d7bc5b1f3533bd8b0504984a49	10	\N
20	2020-11-02 16:31:11.964061+00	2020-11-02 16:31:11.964075+00	uploaded_files/sample_Maccor.xlsx	bc6f07013a09fed8658411f5c894ed40	10	1
21	2020-11-02 16:53:59.690677+00	2020-11-02 16:53:59.690689+00	uploaded_files/sample_Maccor_2.xlsx	7102ac2452d3e22d5cf7148784fccc38	10	\N
22	2020-11-05 15:32:25.079192+00	2020-11-12 18:06:23.18682+00	uploaded_files/C_over_20_run_25_C_CA1.txt	690ea0970ca93096f6a9399829aa631c	10	2
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
5	Ni	Nickel	0
6	LiPF6	LiPF6	151.905
2	C	Carbon	12.011
\.


--
-- Data for Name: dfndb_data; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_data (id, paper_id, user_owner_id, attributes, status, name, notes, modified_on, created_on, slug) FROM stdin;
1	1	1	{}	10	test foo	moo	2020-10-16	2020-10-16 18:01:43.737067+01	bork
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

COPY public.dfndb_material (id, polymer, user_owner_id, type, attributes, status, name, notes, modified_on, created_on, slug) FROM stdin;
2	1	1	1	{}	10	Graphite		2020-10-16	2020-10-16 15:05:13.815326+01	bork
3	0	1	2	{}	10	Lithium Metal		2020-10-16	2020-10-16 15:06:34.982964+01	bork
1	0	1	1	{}	10	NMC622		2020-11-12	2020-10-16 12:16:10.333468+01	nmc622
\.


--
-- Data for Name: dfndb_method; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_method (id, type, description, user_owner_id, attributes, status, name, notes, modified_on, created_on, slug) FROM stdin;
1	2		1	{}	10	DFN		2020-10-16	2020-10-16 14:09:50.498057+01	bork
2	1		1	{}	10	GITT		2020-10-16	2020-10-16 14:10:00.357987+01	bork
3	1000		1	{}	10	My DFN model		2020-10-26	2020-10-26 11:52:26.985926+00	my-dfn-model
4	2000		1	{}	10	My experimental method		2020-10-26	2020-10-26 11:53:05.693795+00	my-experimental-method
\.


--
-- Data for Name: dfndb_parameter; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.dfndb_parameter (id, symbol, notes, unit_id, user_owner_id, attributes, status, name, modified_on, created_on, slug) FROM stdin;
2	t		6	1	{}	10	Thickness	2020-10-16	2020-10-16 13:36:29.748252+01	bork
3	C		9	1	{}	10	Capacity	2020-10-16	2020-10-16 13:51:37.090972+01	bork
1	rP		10	\N	["boing", "boing"]	10	particle radius	2020-10-16	2020-10-16 13:02:34.855802+01	bork
4	V		1	1	{}	10	Cell Voltage	2020-10-28	2020-10-28 14:42:37.150113+00	cell-voltage-v-v
6	C		11	1	{}	10	Capacity	2020-10-30	2020-10-30 12:17:04.438278+00	capacity-c-mah
7	I		5	1	{}	10	Pack Current	2020-10-30	2020-10-30 15:03:05.688117+00	pack-current-i-a
8	x		12	1	{}	10	miscellaneous	2020-11-01	2020-11-01 17:31:08.087297+00	miscellaneous-x-arb
9	T		7	1	{}	10	Thickness	2020-11-12	2020-11-12 16:57:06.835404+00	thickness-t-mm
10	CV		1	1	{}	10	Control Voltage	2020-11-12	2020-11-12 18:08:04.598826+00	control-voltage-cv-v
11	t		13	1	{}	10	Time	2020-11-12	2020-11-12 19:55:19.683333+00	time-t-s
12	x		14	1	{}	10	Sample number	2020-11-12	2020-11-12 19:56:45.386025+00	sample-number-x-x
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
11	Capacity	C	milliAmp Hour	mAh	f	0.0002777777777777778	3
12	Arbitrary	Arb	Arb	Arb	f	\N	\N
13	Time	s	seconds	s	t	\N	\N
14	int	.		x	f	\N	\N
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
14	2020-08-04 19:54:28.563138+01	1	Experiment object (1)	1	[{"added": {}}]	8	1
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
51	2020-08-13 11:32:39.18455+01	3	binbin	2	[{"changed": {"fields": ["is_superuser"]}}]	12	1
70	2020-08-13 15:55:13.379716+01	9	tom/fooo/2020-08-05	2	[{"changed": {"fields": ["analysis"]}}]	8	1
1	2020-08-04 19:13:10.226362+01	1	foo	1	[{"added": {}}]	\N	1
15	2020-08-04 20:17:17.174324+01	1	4s	1	[{"added": {}}]	\N	1
7	2020-08-04 19:42:29.857145+01	1	GalvoTron 3000	1	[{"added": {}}]	\N	1
8	2020-08-04 19:45:01.780472+01	2	GalvoTron 3000	1	[{"added": {}}]	\N	1
71	2020-08-15 16:26:07.435613+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	1	[{"added": {}}]	\N	1
72	2020-08-15 16:26:20.330113+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
50	2020-08-13 10:08:11.60325+01	1	BioLogic_full_u455xrV.txt	1	[{"added": {}}]	\N	1
52	2020-08-13 11:45:05.248666+01	1	BioLogic_full_u455xrV.txt	2	[]	\N	3
53	2020-08-13 11:45:09.003282+01	1	BioLogic_full_u455xrV.txt	2	[]	\N	3
54	2020-08-13 11:45:59.648366+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	\N	3
55	2020-08-13 11:46:07.851905+01	1	bio-logic-data-table.tsv	2	[{"changed": {"fields": ["raw_data_file"]}}]	\N	1
56	2020-08-13 11:46:37.388125+01	1	BioLogic_full_Bq7ABsZ.txt	2	[{"changed": {"fields": ["raw_data_file"]}}]	\N	1
57	2020-08-13 11:47:51.783604+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	1	[{"added": {}}]	\N	3
58	2020-08-13 13:41:16.80162+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	2	[]	\N	1
59	2020-08-13 13:44:28.732886+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	2	[]	\N	1
60	2020-08-13 13:45:10.46911+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_l9X9cj2.mpt	2	[]	\N	1
61	2020-08-13 14:56:13.246066+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_rRcvu3U.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	\N	3
84	2020-08-16 16:02:44.784119+01	6	rishi	1	[{"added": {}}]	12	1
85	2020-08-16 16:03:02.079082+01	6	rishi	2	[{"changed": {"fields": ["is_staff", "is_superuser"]}}]	12	1
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
119	2020-10-14 14:47:38.831365+01	1	None	2	[]	35	1
120	2020-10-14 15:46:13.419807+01	1	52f1021a6e32e4202acab1c5c19f0067cc1ce38a	1	[{"added": {}}]	46	1
130	2020-10-15 16:41:04.55752+01	1	Imperial College	2	[{"changed": {"fields": ["Name", "Status", "Notes", "Is research", "Is mfg cells", "Website"]}}]	34	1
131	2020-10-15 17:38:59.894418+01	1	Person object (1)	2	[{"changed": {"fields": ["Name", "User", "Org"]}}]	36	1
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
214	2020-10-26 11:53:05.695042+00	4	My experimental method	1	[{"added": {}}]	30	1
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
116	2020-10-12 22:00:22.900391+01	1	ExperimentalApparatus object (1)	2	[]	\N	1
121	2020-10-15 12:49:42.377249+01	3	None	3		\N	1
122	2020-10-15 12:49:57.048987+01	2	None	3		\N	1
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
198	2020-10-19 16:59:28.043635+01	1	toward-unique-identifiers-2019	2	[]	35	1
200	2020-10-21 12:34:48.225406+01	2	Bob's company	1	[{"added": {}}]	34	1
206	2020-10-22 11:19:23.723233+01	1	None	1	[{"added": {}}, {"added": {"name": "device config node", "object": "DeviceConfigNode object (1)"}}]	51	1
207	2020-10-22 11:27:04.622444+01	1	None	2	[{"added": {"name": "device config node", "object": "DeviceConfigNode object (2)"}}, {"added": {"name": "device config node", "object": "DeviceConfigNode object (3)"}}, {"added": {"name": "device config node", "object": "DeviceConfigNode object (4)"}}, {"changed": {"name": "device config node", "object": "DeviceConfigNode object (1)", "fields": ["Net name"]}}]	51	1
208	2020-10-22 11:33:41.512118+01	1	2s Module	2	[{"changed": {"fields": ["Name"]}}, {"changed": {"name": "device config node", "object": "2s Module/MiddleCathode", "fields": ["Next"]}}, {"changed": {"name": "device config node", "object": "2s Module/MiddleAnode", "fields": ["Next"]}}]	51	1
209	2020-10-22 11:33:53.214627+01	1	2S Module	2	[{"changed": {"fields": ["Name"]}}]	51	1
210	2020-10-22 11:38:46.195344+01	1	2S Module	2	[{"changed": {"name": "device config node", "object": "2S Module/Pack +vePositive", "fields": ["Device terminal name"]}}, {"changed": {"name": "device config node", "object": "2S Module/MiddleNegative", "fields": ["Device terminal name"]}}, {"changed": {"name": "device config node", "object": "2S Module/MiddlePositive", "fields": ["Device terminal name"]}}, {"changed": {"name": "device config node", "object": "2S Module/Pack -veNegative", "fields": ["Device terminal name"]}}]	51	1
211	2020-10-22 11:43:18.232646+01	1	2S Module	2	[{"changed": {"name": "device config node", "object": "2S Module/Pack +vePositive", "fields": ["Device position id"]}}, {"changed": {"name": "device config node", "object": "2S Module/MiddleNegative", "fields": ["Device position id"]}}, {"changed": {"name": "device config node", "object": "2S Module/MiddlePositive", "fields": ["Device position id"]}}, {"changed": {"name": "device config node", "object": "2S Module/Pack -veNegative", "fields": ["Device position id"]}}]	51	1
212	2020-10-22 11:56:13.735901+01	1	2S Module config	2	[{"changed": {"fields": ["Name"]}}]	51	1
213	2020-10-26 11:52:26.988082+00	3	My DFN model	1	[{"added": {}}]	30	1
352	2020-11-01 14:47:05.838445+00	7	Imperial College None (1 off) 2020-11-01	3		38	1
199	2020-10-21 12:34:11.865153+01	1	None	1	[{"added": {}}]	\N	1
201	2020-10-21 12:36:23.18336+01	2	bob's LiPo	1	[{"added": {}}]	\N	1
215	2020-10-26 12:08:07.604887+00	6	a cell	1	[{"added": {}}]	\N	1
202	2020-10-22 11:13:00.283855+01	3	test 1s LiPo spec	1	[{"added": {}}]	\N	1
203	2020-10-22 11:13:56.650286+01	4	GalvoTron 5000	1	[{"added": {}}]	\N	1
204	2020-10-22 11:16:00.880295+01	5	MyCellSpecification	1	[{"added": {}}]	\N	1
205	2020-10-22 11:16:19.662917+01	5	MyCellSpecification	2	[{"changed": {"fields": ["Attributes"]}}]	\N	1
216	2020-10-26 12:11:37.378668+00	7	a module	1	[{"added": {}}]	\N	1
257	2020-10-27 00:21:55.914815+00	1	None	1	[{"added": {}}, {"added": {"name": "device config node", "object": "None/NoneNone"}}, {"added": {"name": "device config node", "object": "None/NoneNone"}}]	51	1
273	2020-10-28 14:42:37.15201+00	4	Cell Voltage: V / V	1	[{"added": {}}]	32	1
274	2020-10-28 14:49:51.199973+00	1	tom/None/2020-10-28	1	[{"added": {}}, {"added": {"name": "dataset", "object": "A8932-Datasheet.pdf"}}]	8	1
275	2020-10-28 14:53:01.702663+00	1	tom None 2020-10-28	2	[]	8	1
276	2020-10-29 12:46:15.234075+00	1	A8932-Datasheet.pdf	2	[]	23	1
277	2020-10-29 12:46:24.92334+00	1	A8932-Datasheet.pdf	2	[]	23	1
278	2020-10-29 12:47:46.791135+00	2	BioLogic_full_MQSEywk.txt	1	[{"added": {}}]	23	1
279	2020-10-29 12:52:36.593107+00	2	BioLogic_full_MQSEywk.txt	2	[]	23	1
280	2020-10-29 13:32:48.344524+00	97	statelessapp | Can add stateless app	3		10	1
281	2020-10-29 13:32:48.355993+00	98	statelessapp | Can change stateless app	3		10	1
282	2020-10-29 13:32:48.360289+00	99	statelessapp | Can delete stateless app	3		10	1
283	2020-10-29 13:32:48.364037+00	100	statelessapp | Can view stateless app	3		10	1
284	2020-10-29 13:35:00.903608+00	25	statelessapp	3		13	1
285	2020-10-29 13:35:00.914687+00	24	dashapp	3		13	1
286	2020-10-29 13:35:00.918863+00	20	ec_cycle	3		13	1
287	2020-10-29 13:35:00.925169+00	7	experimentalapparatus	3		13	1
288	2020-10-29 13:35:00.931403+00	6	testprotocol	3		13	1
289	2020-10-29 13:35:00.947616+00	5	signaltype	3		13	1
290	2020-10-29 13:35:00.953869+00	4	manufacturer	3		13	1
291	2020-10-29 13:35:00.959997+00	3	equipment	3		13	1
292	2020-10-29 13:35:00.965825+00	2	cellseparator	3		13	1
2	2020-08-04 19:25:35.516012+01	1	BorkCorp	1	[{"added": {}}]	\N	1
4	2020-08-04 19:27:53.921631+01	1	MyMembrane	1	[{"added": {}}]	\N	1
6	2020-08-04 19:41:57.989858+01	2	Maccor	1	[{"added": {}}]	\N	1
9	2020-08-04 19:47:34.828985+01	1	Tom's GalvoTron 3000	1	[{"added": {}}]	\N	1
10	2020-08-04 19:51:08.397906+01	1	PyBaMM example protocol	1	[{"added": {}}]	\N	1
11	2020-08-04 19:52:01.270893+01	1	Tom's Lab	1	[{"added": {}}]	\N	1
13	2020-08-04 19:52:52.127136+01	1	Tom's GalvoTron 3000	2	[{"changed": {"fields": ["type"]}}]	\N	1
87	2020-09-03 19:08:40.505196+01	1	Voltage	1	[{"added": {}}]	\N	1
88	2020-09-03 19:08:49.55247+01	2	Current	1	[{"added": {}}]	\N	1
89	2020-09-03 19:09:08.482438+01	3	Temperature	1	[{"added": {}}]	\N	1
90	2020-09-03 19:09:18.249333+01	4	Time	1	[{"added": {}}]	\N	1
91	2020-09-03 19:12:30.310237+01	4	Time	2	[{"changed": {"fields": ["unit"]}}]	\N	1
92	2020-09-03 19:16:46.720441+01	4	Time/s	2	[{"changed": {"fields": ["unit_symbol"]}}]	\N	1
93	2020-09-03 19:17:17.039241+01	3	Temperature/°C	2	[{"changed": {"fields": ["unit_symbol"]}}]	\N	1
94	2020-09-03 19:17:33.724311+01	2	Current/A	2	[{"changed": {"fields": ["unit_name", "unit_symbol"]}}]	\N	1
95	2020-09-03 19:17:40.814297+01	3	Temperature/°C	2	[{"changed": {"fields": ["unit_name"]}}]	\N	1
96	2020-09-03 19:18:31.397625+01	1	Voltage/V	2	[{"changed": {"fields": ["unit_name", "unit_symbol"]}}]	\N	1
97	2020-09-03 19:18:54.762396+01	5	Power/W	1	[{"added": {}}]	\N	1
256	2020-10-27 00:21:30.75437+00	1	My Cell Spec	1	[{"added": {}}]	\N	1
258	2020-10-27 11:27:15.178955+00	2	My NMC622 2s2p Module	1	[{"added": {}}, {"added": {"name": "thing", "object": "Cell A1"}}, {"added": {"name": "thing", "object": "Cell A2"}}, {"added": {"name": "thing", "object": "Cell B1"}}, {"added": {"name": "thing", "object": "Cell B2"}}]	\N	1
263	2020-10-27 11:38:38.412709+00	2	My NMC622 2s2p Module	2	[{"added": {"name": "thing", "object": "Cell A1"}}, {"added": {"name": "thing", "object": "Cell A2"}}, {"added": {"name": "thing", "object": "Cell B1"}}, {"added": {"name": "thing", "object": "Cell B2"}}]	\N	1
268	2020-10-27 11:40:50.472164+00	2	My NMC622 2s2p Module	2	[{"added": {"name": "device", "object": "Cell A1"}}, {"added": {"name": "device", "object": "Cell A2"}}]	\N	1
269	2020-10-27 11:41:01.29575+00	2	My NMC622 2s2p Module	2	[{"added": {"name": "device", "object": "Cell B1"}}, {"added": {"name": "device", "object": "Cell B2"}}]	\N	1
271	2020-10-28 11:30:16.70413+00	11	Cell A1	2	[{"changed": {"fields": ["Specification"]}}]	\N	1
272	2020-10-28 11:30:30.554495+00	2	My NMC622 2s2p Module	2	[{"changed": {"name": "device", "object": "Cell A2", "fields": ["Specification"]}}, {"changed": {"name": "device", "object": "Cell B1", "fields": ["Specification"]}}, {"changed": {"name": "device", "object": "Cell B2", "fields": ["Specification"]}}]	\N	1
117	2020-10-12 23:22:21.079795+01	1	ExperimentalApparatus object (1)	2	[{"changed": {"fields": ["Attributes"]}}]	\N	1
118	2020-10-12 23:26:31.741966+01	1	None	2	[]	\N	1
132	2020-10-15 17:55:03.068903+01	1	Tom's GalvoTron 5000	2	[{"changed": {"fields": ["Name"]}}]	\N	1
293	2020-10-30 11:08:16.57592+00	15	Generic Cell	1	[{"added": {}}, {"added": {"name": "device specification", "object": "Positive Electrode"}}, {"added": {"name": "device specification", "object": "Negative Electrode"}}, {"added": {"name": "device specification", "object": "Electrolyte"}}, {"added": {"name": "device specification", "object": "Separator"}}, {"added": {"name": "device parameter", "object": "Thickness: t / m"}}]	61	1
294	2020-10-30 11:19:28.772555+00	15	Generic Cell	2	[]	61	1
295	2020-10-30 11:30:54.689434+00	18	Electrolyte	2	[{"changed": {"fields": ["Abstract Specification"]}}]	61	1
296	2020-10-30 11:31:02.680849+00	19	Separator	2	[{"changed": {"fields": ["Abstract Specification"]}}]	61	1
297	2020-10-30 11:49:08.862264+00	15	Generic Cell	2	[]	61	1
298	2020-10-30 11:51:24.625293+00	15	Generic Cell	2	[]	61	1
299	2020-10-30 12:13:43.480626+00	11	Capacity (C) / mAh	1	[{"added": {}}]	31	1
300	2020-10-30 12:17:04.43993+00	6	Capacity: C / mAh	1	[{"added": {}}]	32	1
301	2020-10-30 12:17:54.383898+00	20	My NMC622 Cell	1	[{"added": {}}, {"added": {"name": "device parameter", "object": "Capacity: C / mAh"}}]	61	1
302	2020-10-30 12:18:38.515635+00	20	My NMC622 Cell	2	[{"changed": {"fields": ["Device type"]}}]	61	1
303	2020-10-30 12:18:56.130867+00	15	Cell	2	[{"changed": {"fields": ["Name"]}}]	61	1
304	2020-10-30 12:20:54.357144+00	21	Generic	1	[{"added": {}}]	61	1
305	2020-10-30 12:21:03.012958+00	15	Cell	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
306	2020-10-30 12:21:18.167948+00	21	Generic	2	[{"changed": {"fields": ["tree_id"]}}]	61	1
307	2020-10-30 12:21:59.967302+00	21	Generic	2	[{"changed": {"fields": ["Abstract Specification"]}}]	61	1
308	2020-10-30 13:06:04.634166+00	22	None	1	[{"added": {}}]	38	1
309	2020-10-30 13:28:23.30797+00	58	devicelist	3		13	1
310	2020-10-30 13:33:16.212254+00	23	2s2p module	1	[{"added": {}}, {"added": {"name": "device specification", "object": "Cell 1A"}}, {"added": {"name": "device specification", "object": "Cell 1B"}}, {"added": {"name": "device specification", "object": "Cell 2A"}}, {"added": {"name": "device specification", "object": "Cell 2B"}}]	61	1
311	2020-10-30 13:49:29.4837+00	21	Generic	2	[{"added": {"name": "device specification", "object": "Module"}}, {"added": {"name": "device specification", "object": "Pack"}}]	61	1
312	2020-10-30 13:50:00.069559+00	15	Cell	2	[{"changed": {"fields": ["parent", "lft", "rght", "level"]}}]	61	1
313	2020-10-30 13:51:23.240124+00	29	Pack	3		61	1
314	2020-10-30 14:33:45.88438+00	16	Positive Electrode	2	[{"changed": {"fields": ["Attributes"]}}]	61	1
315	2020-10-30 14:36:14.88364+00	16	Positive Electrode	2	[{"changed": {"fields": ["Attributes"]}}]	61	1
316	2020-10-30 14:36:44.453657+00	16	Positive Electrode	2	[{"changed": {"fields": ["Attributes"]}}]	61	1
317	2020-10-30 14:51:53.237978+00	16	Positive Electrode	2	[]	61	1
318	2020-10-30 14:58:58.470294+00	23	2s2p module	2	[{"changed": {"fields": ["Complete"]}}]	61	1
319	2020-10-30 14:59:03.033927+00	20	My NMC622 Cell	2	[{"changed": {"fields": ["Complete"]}}]	61	1
320	2020-10-30 14:59:54.19131+00	1	tom None 2020-10-28	2	[{"changed": {"fields": ["Device", "Protocol"]}}]	8	1
321	2020-10-30 15:01:02.902142+00	15	Cell	2	[{"changed": {"name": "device parameter", "object": "Cell Voltage: V / V", "fields": ["Name", "Parameter"]}}]	61	1
322	2020-10-30 15:02:17.217956+00	15	Cell	2	[]	61	1
323	2020-10-30 15:03:05.689261+00	7	Pack Current: I / A	1	[{"added": {}}]	32	1
324	2020-10-30 15:03:15.398613+00	28	Module	2	[{"added": {"name": "device parameter", "object": "Pack Current: I / A"}}]	61	1
325	2020-10-30 15:05:31.984399+00	22	My NMC622 Cell 1	2	[{"changed": {"fields": ["Name"]}}]	38	1
326	2020-10-30 15:06:29.93398+00	30	2s2p module batch of 100	1	[{"added": {}}]	38	1
327	2020-11-01 14:06:01.077976+00	2	BioLogic_full_57G6K9u_5aEH9qc.txt	1	[{"added": {}}]	63	1
328	2020-11-01 14:09:15.116161+00	2	tom foo 2020-11-01	1	[{"added": {}}, {"added": {"name": "dataset", "object": "BioLogic_full_57G6K9u_5aEH9qc.txt"}}]	8	1
329	2020-11-01 14:17:47.634037+00	2	tom foo 2020-11-01	2	[]	8	1
330	2020-11-01 14:33:34.000053+00	3	tom None 2020-11-01	1	[{"added": {}}, {"added": {"name": "dataset", "object": "BioLogic_full_57G6K9u_5aEH9qc.txt"}}]	8	1
331	2020-11-01 14:39:48.750072+00	1	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
332	2020-11-01 14:40:16.732717+00	2	BioLogic_full_57G6K9u_5aEH9qc.txt	2	[{"added": {"name": "Column Mapping", "object": "DataColumn object (1)"}}]	23	1
333	2020-11-01 14:40:26.130318+00	2	BioLogic_full_57G6K9u_5aEH9qc.txt	2	[{"changed": {"name": "Column Mapping", "object": "DataColumn object (1)", "fields": ["Device"]}}]	23	1
334	2020-11-01 14:40:35.780654+00	1	Imperial College None (1 off) 2020-11-01	2	[{"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
335	2020-11-01 14:40:42.175008+00	2	BioLogic_full_57G6K9u_5aEH9qc.txt	2	[{"changed": {"name": "Column Mapping", "object": "DataColumn object (1)", "fields": ["Device"]}}]	23	1
336	2020-11-01 14:41:23.486257+00	2	Imperial College None (1 off) 2020-11-01	3		38	1
337	2020-11-01 14:41:23.519545+00	3	Imperial College None (1 off) 2020-11-01	3		38	1
338	2020-11-01 14:42:27.760594+00	3	BioLogic_full_57G6K9u_5aEH9qc.txt	1	[{"added": {}}]	23	1
339	2020-11-01 14:42:37.519639+00	3	BioLogic_full_57G6K9u_5aEH9qc.txt	2	[]	23	1
340	2020-11-01 14:42:41.575044+00	3	BioLogic_full_57G6K9u_5aEH9qc.txt	2	[]	23	1
341	2020-11-01 14:42:55.055273+00	1	bork	1	[{"added": {}}]	61	1
342	2020-11-01 14:42:59.208785+00	1	bork	2	[]	61	1
343	2020-11-01 14:43:04.074624+00	3	BioLogic_full_57G6K9u_5aEH9qc.txt	2	[]	23	1
344	2020-11-01 14:43:08.813336+00	1	Imperial College None (1 off) 2020-11-01	2	[{"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
345	2020-11-01 14:46:31.069975+00	4	Imperial College None (1 off) 2020-11-01	2	[{"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
346	2020-11-01 14:46:37.223763+00	1	Imperial College None (1 off) 2020-11-01	2	[{"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
347	2020-11-01 14:46:50.613405+00	1	Imperial College None (1 off) 2020-11-01	3		38	1
348	2020-11-01 14:46:50.628821+00	4	Imperial College None (1 off) 2020-11-01	3		38	1
349	2020-11-01 14:46:50.640182+00	5	Imperial College None (1 off) 2020-11-01	3		38	1
350	2020-11-01 14:46:50.651077+00	6	Imperial College None (1 off) 2020-11-01	3		38	1
351	2020-11-01 14:46:55.344219+00	7	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
353	2020-11-01 14:47:05.87836+00	8	Imperial College None (1 off) 2020-11-01	3		38	1
354	2020-11-01 14:47:15.397273+00	9	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
355	2020-11-01 14:47:54.795184+00	9	Imperial College None (1 off) 2020-11-01	3		38	1
356	2020-11-01 14:47:54.823996+00	10	Imperial College None (1 off) 2020-11-01	3		38	1
357	2020-11-01 15:10:57.566664+00	11	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
358	2020-11-01 15:11:14.590871+00	11	Imperial College None (1 off) 2020-11-01	3		38	1
359	2020-11-01 15:11:14.612191+00	12	Imperial College None (1 off) 2020-11-01	3		38	1
360	2020-11-01 15:11:20.868189+00	13	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
361	2020-11-01 15:11:35.059812+00	13	Imperial College None (1 off) 2020-11-01	3		38	1
362	2020-11-01 15:11:35.097733+00	14	Imperial College None (1 off) 2020-11-01	3		38	1
363	2020-11-01 15:11:44.536983+00	15	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
364	2020-11-01 15:12:12.547653+00	2	foo	1	[{"added": {}}]	61	1
365	2020-11-01 15:12:20.168684+00	15	Imperial College None (1 off) 2020-11-01	3		38	1
366	2020-11-01 15:12:20.195695+00	16	Imperial College None (1 off) 2020-11-01	3		38	1
367	2020-11-01 15:12:28.654333+00	17	Imperial College foo (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
368	2020-11-01 15:14:00.502337+00	19	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
369	2020-11-01 15:14:15.882377+00	21	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
370	2020-11-01 15:15:58.406989+00	23	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
371	2020-11-01 15:16:06.508326+00	17	Imperial College foo (1 off) 2020-11-01	3		38	1
372	2020-11-01 15:16:06.541957+00	18	Imperial College None (1 off) 2020-11-01	3		38	1
373	2020-11-01 15:16:06.569243+00	19	Imperial College None (1 off) 2020-11-01	3		38	1
374	2020-11-01 15:16:06.6004+00	20	Imperial College None (1 off) 2020-11-01	3		38	1
375	2020-11-01 15:16:06.627232+00	21	Imperial College None (1 off) 2020-11-01	3		38	1
376	2020-11-01 15:16:06.658069+00	22	Imperial College None (1 off) 2020-11-01	3		38	1
377	2020-11-01 15:16:06.67683+00	23	Imperial College None (1 off) 2020-11-01	3		38	1
378	2020-11-01 15:16:06.690077+00	24	Imperial College None (1 off) 2020-11-01	3		38	1
379	2020-11-01 15:16:09.947659+00	25	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
380	2020-11-01 15:16:23.323012+00	25	Imperial College None (1 off) 2020-11-01	3		38	1
381	2020-11-01 15:16:23.339625+00	26	Imperial College None (1 off) 2020-11-01	3		38	1
382	2020-11-01 15:17:15.635047+00	28	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}, {"added": {"name": "Device or Batch", "object": "Imperial College None (1 off) 2020-11-01"}}]	38	1
383	2020-11-01 15:17:37.295761+00	27	Imperial College None (1 off) 2020-11-01	3		38	1
384	2020-11-01 15:17:37.322098+00	28	Imperial College None (1 off) 2020-11-01	3		38	1
385	2020-11-01 15:17:37.337556+00	29	Imperial College None (1 off) 2020-11-01	3		38	1
386	2020-11-01 15:17:39.868059+00	30	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}]	38	1
387	2020-11-01 15:20:20.482383+00	3	None	1	[{"added": {}}]	61	1
388	2020-11-01 15:20:28.140146+00	1	bork	2	[]	61	1
389	2020-11-01 15:20:43.758379+00	1	bork	2	[]	61	1
390	2020-11-01 16:26:13.936009+00	2	tom foo 2020-11-01	2	[{"deleted": {"name": "dataset", "object": "BioLogic_full_57G6K9u_5aEH9qc.txt"}}]	8	1
391	2020-11-01 16:29:08.983187+00	2	BioLogic_full_57G6K9u_5aEH9qc.txt	3		63	1
392	2020-11-01 16:29:33.949882+00	4	BioLogic_full_aa5m9sL.txt	1	[{"added": {}}]	63	1
393	2020-11-01 16:35:14.589558+00	4	BioLogic_full_aa5m9sL.txt	1	[{"added": {}}]	23	1
394	2020-11-01 16:35:21.070029+00	5	BioLogic_full_aa5m9sL.txt	1	[{"added": {}}]	23	1
395	2020-11-01 16:37:27.67319+00	2	None	3		23	1
396	2020-11-01 16:37:27.684001+00	1	None	3		23	1
397	2020-11-01 17:23:43.861327+00	1	bork	3		61	1
398	2020-11-01 17:23:43.907393+00	2	foo	3		61	1
399	2020-11-01 17:23:43.950273+00	3	None	3		61	1
400	2020-11-01 17:25:16.063612+00	4	Generic Pack	1	[{"added": {}}, {"added": {"name": "device specification", "object": "Generic Module"}}, {"added": {"name": "device parameter", "object": "Capacity: C / Wh"}}]	61	1
401	2020-11-01 17:26:46.442668+00	5	Generic Module	2	[{"added": {"name": "device parameter", "object": "Capacity: C / Wh"}}]	61	1
402	2020-11-01 17:27:16.426389+00	5	Generic Module	2	[{"added": {"name": "device specification", "object": "Generic Cell"}}]	61	1
403	2020-11-01 17:27:37.142627+00	6	Generic Cell	2	[{"added": {"name": "device parameter", "object": "Capacity: C / Wh"}}]	61	1
404	2020-11-01 17:30:10.24309+00	12	Arbitrary (Arb) / Arb	1	[{"added": {}}]	31	1
405	2020-11-01 17:30:24.802193+00	12	Arbitrary (Arb) / Arb	2	[{"changed": {"fields": ["UnitName"]}}]	31	1
406	2020-11-01 17:30:34.805078+00	12	Arbitrary (Arb) / Arb	2	[{"changed": {"fields": ["UnitName"]}}]	31	1
407	2020-11-01 17:30:41.52961+00	12	Arbitrary (Arb) / Arb	2	[{"changed": {"fields": ["UnitName"]}}]	31	1
408	2020-11-01 17:31:08.089968+00	8	miscellaneous: x / Arb	1	[{"added": {}}]	32	1
409	2020-11-01 17:34:50.952972+00	3	tom None 2020-11-01	3		8	1
410	2020-11-01 17:34:50.967583+00	2	tom foo 2020-11-01	3		8	1
411	2020-11-01 17:34:58.973983+00	30	Imperial College None (1 off) 2020-11-01	3		38	1
412	2020-11-01 17:36:29.296296+00	7	My NMC622 Cell	1	[{"added": {}}]	61	1
413	2020-11-01 17:37:40.648053+00	31	Imperial College None (1 off) 2020-11-01	1	[{"added": {}}]	38	1
414	2020-11-01 17:37:52.12403+00	31	Imperial College None (1 off) 2020-11-01	3		38	1
415	2020-11-01 17:41:49.157464+00	32	Imperial College My NMC622 Cell (1 off) 2020-11-01	1	[{"added": {}}]	38	1
416	2020-11-01 17:43:36.327178+00	5	tom My experiment 2020-11-01	1	[{"added": {}}]	8	1
417	2020-11-01 17:45:04.963977+00	8	My NMC622 Module	1	[{"added": {}}]	61	1
418	2020-11-01 17:45:15.293214+00	8	My NMC622 Module	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
419	2020-11-01 17:45:33.656546+00	8	My NMC622 Module	2	[{"changed": {"fields": ["parent", "lft", "rght", "level"]}}]	61	1
420	2020-11-01 17:45:38.383806+00	7	My NMC622 Cell	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
421	2020-11-01 17:45:38.397246+00	7	My NMC622 Cell	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
422	2020-11-01 17:46:25.83621+00	7	My NMC622 Cell	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
423	2020-11-01 17:46:29.4334+00	7	My NMC622 Cell	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
424	2020-11-01 17:51:09.570345+00	56	thing	3		13	1
425	2020-11-01 17:51:09.582122+00	55	thingcomposition	3		13	1
426	2020-11-01 17:51:09.58809+00	54	compositedevice	3		13	1
427	2020-11-01 17:51:09.593842+00	53	moduledevice	3		13	1
428	2020-11-01 17:51:09.599668+00	52	basemodelwithslug	3		13	1
217	2020-10-26 14:19:59.406685+00	1	pack	1	[{"added": {}}, {"added": {"name": "thing", "object": "Cell 1"}}, {"added": {"name": "thing", "object": "Cell 2"}}]	\N	1
218	2020-10-26 14:21:02.988101+00	3	Cell 2	2	[{"changed": {"fields": ["lft", "rght"]}}]	\N	1
219	2020-10-26 14:21:06.718299+00	3	Cell 2	2	[{"changed": {"fields": ["parent", "lft", "rght", "level"]}}]	\N	1
220	2020-10-26 14:21:39.75855+00	3	Cell 2	2	[{"changed": {"fields": ["parent", "lft", "rght", "level"]}}]	\N	1
221	2020-10-26 14:21:44.666408+00	2	Cell 1	2	[{"changed": {"fields": ["lft", "rght"]}}]	\N	1
222	2020-10-26 14:22:28.077301+00	2	Cell 1	2	[{"changed": {"fields": ["Parent"]}}, {"added": {"name": "thing", "object": "PositiveElectrode"}}]	\N	1
223	2020-10-26 14:23:59.310044+00	2	Cell 1	2	[{"changed": {"fields": ["Is composite"]}}]	\N	1
224	2020-10-26 14:24:04.314103+00	1	pack	2	[{"changed": {"fields": ["Is composite"]}}]	\N	1
225	2020-10-26 14:24:11.597249+00	2	Cell 1	2	[{"changed": {"fields": ["Parent"]}}]	\N	1
226	2020-10-26 14:25:10.117402+00	3	Cell 2	2	[{"added": {"name": "thing", "object": "PositiveElectrode"}}, {"added": {"name": "thing", "object": "NegativeElectrode"}}]	\N	1
227	2020-10-26 14:25:18.384065+00	2	Cell 1	2	[{"added": {"name": "thing", "object": "NegativeElectrode"}}]	\N	1
228	2020-10-26 14:25:43.682137+00	1	2S Pack	2	[{"changed": {"fields": ["Name"]}}]	\N	1
229	2020-10-26 14:27:04.015632+00	8	My Batch	1	[{"added": {}}]	\N	1
230	2020-10-26 14:27:11.893738+00	1	2S Pack	2	[{"changed": {"fields": ["Parent"]}}]	\N	1
231	2020-10-26 14:27:26.371091+00	1	2S Pack	2	[{"changed": {"fields": ["Is specification"]}}]	\N	1
232	2020-10-26 14:28:49.550933+00	1	2S Module	2	[{"changed": {"fields": ["Name"]}}]	\N	1
233	2020-10-26 14:30:48.491003+00	8	My Module	2	[{"changed": {"fields": ["Name"]}}]	\N	1
234	2020-10-26 14:30:56.382136+00	8	My Pack	2	[{"changed": {"fields": ["Name"]}}]	\N	1
235	2020-10-26 14:31:12.764119+00	8	My Pack	2	[{"changed": {"fields": ["Is specification"]}}]	\N	1
236	2020-10-26 14:32:00.704136+00	9	Pack Clone	1	[{"added": {}}]	\N	1
237	2020-10-26 16:21:44.441835+00	6	NegativeElectrode	2	[{"changed": {"fields": ["Is composite"]}}]	\N	1
238	2020-10-26 16:21:58.668651+00	5	PositiveElectrode	2	[{"changed": {"fields": ["Is composite"]}}]	\N	1
239	2020-10-26 16:29:08.691665+00	6	NegativeElectrode	2	[{"added": {"name": "thing", "object": "foo"}}]	\N	1
240	2020-10-26 16:29:41.11374+00	3	Cell 2	2	[{"changed": {"fields": ["Is composite"]}}]	\N	1
241	2020-10-26 16:30:08.247457+00	8	My Pack	3		\N	1
242	2020-10-26 16:30:38.113092+00	8	My Pack	3		\N	1
243	2020-10-26 16:30:38.136902+00	1	2S Module	3		\N	1
244	2020-10-26 16:30:38.151424+00	3	Cell 2	3		\N	1
245	2020-10-26 16:30:38.166317+00	5	PositiveElectrode	3		\N	1
246	2020-10-26 16:30:38.18824+00	6	NegativeElectrode	3		\N	1
247	2020-10-26 16:30:38.211684+00	10	foo	3		\N	1
248	2020-10-26 16:30:38.229517+00	2	Cell 1	3		\N	1
249	2020-10-26 16:30:38.249766+00	4	PositiveElectrode	3		\N	1
250	2020-10-26 16:30:38.26269+00	7	NegativeElectrode	3		\N	1
251	2020-10-26 16:30:38.273716+00	9	Pack Clone	3		\N	1
252	2020-10-26 16:31:06.604435+00	11	My Module	1	[{"added": {}}, {"added": {"name": "thing", "object": "Cell 1"}}, {"added": {"name": "thing", "object": "Cell 2"}}]	\N	1
253	2020-10-26 16:31:18.650988+00	12	Cell 1	2	[{"changed": {"fields": ["Parent assembly"]}}, {"added": {"name": "thing", "object": "PositiveElectrode"}}]	\N	1
254	2020-10-26 16:32:25.60542+00	12	Cell 1	2	[{"changed": {"fields": ["Parent assembly"]}}]	\N	1
255	2020-10-26 16:33:20.829772+00	12	Cell 1	2	[{"changed": {"fields": ["lft", "rght"]}}]	\N	1
259	2020-10-27 11:27:47.258646+00	3	Cell A1	3		\N	1
260	2020-10-27 11:27:47.273921+00	4	Cell A2	3		\N	1
261	2020-10-27 11:27:47.286354+00	5	Cell B1	3		\N	1
262	2020-10-27 11:27:47.30147+00	6	Cell B2	3		\N	1
264	2020-10-27 11:38:58.55007+00	7	Cell A1	3		\N	1
265	2020-10-27 11:38:58.587016+00	8	Cell A2	3		\N	1
266	2020-10-27 11:38:58.613523+00	9	Cell B1	3		\N	1
267	2020-10-27 11:38:58.64213+00	10	Cell B2	3		\N	1
270	2020-10-27 11:43:39.926131+00	12	Cell A2	2	[{"changed": {"fields": ["Status"]}}]	\N	1
5	2020-08-04 19:28:19.927154+01	1	MyLiPo	1	[{"added": {}}]	\N	1
3	2020-08-04 19:26:04.905071+01	1	foo	2	[{"changed": {"fields": ["manufacturer"]}}]	\N	1
12	2020-08-04 19:52:35.233623+01	1	GalvoTron 3000	3		\N	1
73	2020-08-15 16:27:19.328572+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
74	2020-08-15 16:29:00.149786+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
75	2020-08-15 16:35:13.104076+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
76	2020-08-15 16:44:43.695498+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
77	2020-08-15 22:01:36.300505+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
78	2020-08-15 22:02:36.949811+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
79	2020-08-15 22:04:51.218447+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
80	2020-08-15 22:05:28.350057+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
81	2020-08-15 22:15:17.813728+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
82	2020-08-15 22:15:35.627463+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
86	2020-08-17 13:09:14.120233+01	1	200720_C-rate_test_Co5_cells_1-14_D128_CD1_a0fZder.mpt	2	[]	\N	1
62	2020-08-13 15:42:26.567344+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_rRcvu3U.mpt	2	[]	\N	1
63	2020-08-13 15:43:05.748529+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_xETlkXH.mpt	1	[{"added": {}}]	\N	1
64	2020-08-13 15:43:11.157068+01	2	200720_C-rate_test_Co5_cells_1-14_D128_CD1_rRcvu3U.mpt	2	[]	\N	1
65	2020-08-13 15:43:45.614216+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_oa7otTL.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	\N	1
66	2020-08-13 15:46:34.261891+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lj6rngx.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	\N	1
67	2020-08-13 15:52:59.611491+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lj6rngx.mpt	2	[]	\N	1
68	2020-08-13 15:53:09.682091+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lvMpGzm.mpt	2	[{"changed": {"fields": ["raw_data_file"]}}]	\N	1
69	2020-08-13 15:54:23.605556+01	3	200720_C-rate_test_Co5_cells_1-14_D128_CD1_lvMpGzm.mpt	2	[{"changed": {"fields": ["experiment"]}}]	\N	1
123	2020-10-15 12:49:57.053634+01	1	None	3		\N	1
124	2020-10-15 13:04:19.151885+01	4	foo	1	[{"added": {}}]	\N	1
125	2020-10-15 13:04:57.852735+01	4	foo	2	[{"changed": {"fields": ["Raw data file"]}}]	\N	1
126	2020-10-15 13:05:13.279474+01	4	foo	2	[{"changed": {"fields": ["Raw data file"]}}]	\N	1
127	2020-10-15 13:09:03.892766+01	6	None	1	[{"added": {}}]	\N	1
128	2020-10-15 13:09:19.458002+01	6	None	2	[{"changed": {"fields": ["Raw data file"]}}]	\N	1
129	2020-10-15 13:12:07.30048+01	6	None	2	[{"changed": {"fields": ["Raw data file"]}}]	\N	1
429	2020-11-01 17:57:20.000469+00	2	Experimenters	2	[{"changed": {"fields": ["Permissions"]}}]	11	1
430	2020-11-01 17:58:20.641264+00	5	BioLogic_full_aa5m9sL.txt	2	[{"changed": {"fields": ["Experiment"]}}]	23	1
431	2020-11-01 17:59:14.441735+00	4	BioLogic_full_aa5m9sL.txt	3		23	1
432	2020-11-01 18:16:16.008256+00	4	BioLogic_full_aa5m9sL.txt	3		63	1
433	2020-11-01 18:16:57.042576+00	11	fooo_DQmKXFM.bork	3		63	1
434	2020-11-01 18:17:13.966111+00	12	fooo_NcJZZ7Y.bork	3		63	1
435	2020-11-01 18:19:06.967877+00	15	fooo_kbMdTS4.bork	3		63	1
436	2020-11-01 18:19:10.54575+00	14	fooo_9DyQn70.bork	3		63	1
437	2020-11-01 18:20:31.85637+00	16	fooo_DCjYSeo.bork	3		63	1
438	2020-11-01 18:58:40.518335+00	5	None	2	[{"changed": {"fields": ["files"]}}]	23	1
439	2020-11-01 18:58:49.216786+00	5	None	2	[{"changed": {"fields": ["files"]}}]	23	1
440	2020-11-01 18:59:15.26785+00	5	mug.jpeg	2	[{"changed": {"fields": ["Raw data file"]}}]	23	1
441	2020-11-02 01:30:55.135047+00	5	mug.jpeg	2	[]	23	1
442	2020-11-02 01:31:02.74165+00	5	mug.jpeg	2	[]	23	1
443	2020-11-02 01:31:06.981653+00	5	mug.jpeg	2	[]	23	1
444	2020-11-02 01:31:47.696071+00	5	mug.jpeg	2	[]	23	1
445	2020-11-02 01:32:43.911531+00	5	mug.jpeg	2	[]	23	1
446	2020-11-02 10:16:51.189801+00	5	mug.jpeg	2	[]	23	1
447	2020-11-02 10:17:01.624415+00	5	mug.jpeg	2	[]	23	1
448	2020-11-02 10:56:01.71074+00	5	tom My experiment 2020-11-01	2	[]	8	1
449	2020-11-02 10:57:30.228593+00	5	tom My experiment 2020-11-01	2	[]	8	1
450	2020-11-02 10:58:05.989594+00	5	tom My experiment 2020-11-01	2	[]	8	1
451	2020-11-02 10:58:17.648788+00	5	tom My experiment 2020-11-01	2	[]	8	1
452	2020-11-02 10:59:35.651467+00	18	BioLogic_full.txt	1	[{"added": {}}]	63	1
453	2020-11-02 11:01:41.654257+00	8	BioLogic_full.txt	1	[{"added": {}}]	23	1
454	2020-11-02 11:04:56.698638+00	8	BioLogic_full.txt	2	[]	23	1
455	2020-11-02 11:05:46.903776+00	8	BioLogic_full.txt	2	[]	23	1
456	2020-11-02 12:00:07.29328+00	6	Cell	2	[{"changed": {"fields": ["Name"]}}]	61	1
457	2020-11-02 12:00:20.870684+00	4	Pack	2	[{"changed": {"fields": ["Name"]}}]	61	1
458	2020-11-02 12:00:27.954151+00	5	Module	2	[{"changed": {"fields": ["Name"]}}]	61	1
459	2020-11-02 12:13:32.257089+00	1	2s2p arrangement	1	[{"added": {}}, {"added": {"name": "device config node", "object": "2s2p arrangement/NoneNone"}}]	51	1
460	2020-11-02 12:16:18.681188+00	6	Cell	2	[{"added": {"name": "device specification", "object": "Positive Electrode"}}, {"added": {"name": "device specification", "object": "Negative Electrode"}}, {"added": {"name": "device specification", "object": "Separator"}}, {"added": {"name": "device specification", "object": "Electrolyte"}}]	61	1
461	2020-11-02 12:18:39.034302+00	9	Positive Electrode	2	[{"added": {"name": "device specification", "object": "Positive Electrode Material"}}]	61	1
462	2020-11-02 12:19:21.470078+00	10	Negative Electrode	2	[{"added": {"name": "device specification", "object": "Neg. E'trode Material"}}]	61	1
463	2020-11-02 12:19:46.362799+00	13	Pos. E'trode Material	2	[{"changed": {"fields": ["Name"]}}]	61	1
464	2020-11-02 12:20:17.381855+00	11	Separator	2	[{"added": {"name": "device specification", "object": "Separator Material"}}]	61	1
465	2020-11-02 12:20:56.097846+00	6	Cell	2	[{"added": {"name": "device specification", "object": "Cell Casing"}}]	61	1
466	2020-11-02 12:21:50.620177+00	1	2s2p arrangement	2	[{"added": {"name": "device config node", "object": "2s2p arrangement/NoneNone"}}]	51	1
467	2020-11-02 12:22:29.693808+00	1	2s2p arrangement	2	[{"changed": {"name": "device config node", "object": "2s2p arrangement/None+", "fields": ["Device position id", "Device terminal name"]}}]	51	1
468	2020-11-02 12:22:56.461409+00	1	2s2p arrangement	2	[{"changed": {"name": "device config node", "object": "2s2p arrangement/V1+", "fields": ["Net name"]}}]	51	1
469	2020-11-02 12:25:59.376162+00	1	2s2p arrangement	3		51	1
470	2020-11-02 12:35:00.341082+00	4	2s2p module arrangement	1	[{"added": {}}, {"added": {"name": "device config node", "object": "2s2p module arrangement/Cell_A1"}}, {"added": {"name": "device config node", "object": "2s2p module arrangement/Cell_A2"}}]	51	1
471	2020-11-02 12:36:30.132803+00	4	2s2p module arrangement	2	[{"added": {"name": "device config node", "object": "2s2p module arrangement/Cell_B1"}}, {"added": {"name": "device config node", "object": "2s2p module arrangement/Cell_B2"}}, {"added": {"name": "device config node", "object": "2s2p module arrangement/Module_DEVICE"}}]	51	1
472	2020-11-02 12:42:33.456941+00	6	Cell	2	[{"changed": {"fields": ["Complete"]}}]	61	1
473	2020-11-02 12:42:40.327458+00	5	Module	2	[{"changed": {"fields": ["Complete"]}}]	61	1
474	2020-11-02 12:42:46.849029+00	4	Pack	2	[{"changed": {"fields": ["Complete"]}}]	61	1
475	2020-11-02 12:50:39.396617+00	4	2s2p module	2	[{"changed": {"fields": ["Name"]}}]	51	1
476	2020-11-02 12:51:41.166881+00	4	2s2p module	2	[{"deleted": {"name": "device config node", "object": "2s2p module/Module_DEVICE"}}]	51	1
477	2020-11-02 12:52:36.101022+00	5	Module	2	[{"added": {"name": "device specification", "object": "Terminal"}}]	61	1
478	2020-11-02 12:52:59.707838+00	4	Pack	2	[{"added": {"name": "device specification", "object": "Connector"}}]	61	1
479	2020-11-02 12:54:35.47199+00	4	2s2p module	2	[{"added": {"name": "device config node", "object": "2s2p module/Terminal_DEVICE"}}, {"added": {"name": "device config node", "object": "2s2p module/Terminal_DEVICE"}}]	51	1
480	2020-11-02 12:55:22.47645+00	4	2s2p module	2	[{"added": {"name": "device config node", "object": "2s2p module/Terminal_DEVICE"}}]	51	1
481	2020-11-02 12:55:45.343907+00	4	2s2p module	2	[{"changed": {"name": "device config node", "object": "2s2p module/Terminal_MODULE", "fields": ["Device position id"]}}, {"changed": {"name": "device config node", "object": "2s2p module/Terminal_MODULE", "fields": ["Device position id"]}}, {"changed": {"name": "device config node", "object": "2s2p module/Terminal_MODULE", "fields": ["Device position id"]}}]	51	1
547	2020-11-12 17:34:46.57093+00	1	NMC622	2	[{"added": {"name": "composition part", "object": "Li1"}}]	29	1
548	2020-11-12 17:35:00.550959+00	1	NMC622	2	[{"deleted": {"name": "composition part", "object": "Li1"}}]	29	1
482	2020-11-02 12:56:54.506224+00	4	2s2p module	2	[{"changed": {"name": "device config node", "object": "2s2p module/Terminal_+", "fields": ["Device position id", "Pos netname"]}}, {"changed": {"name": "device config node", "object": "2s2p module/Terminal_-", "fields": ["Device position id", "Pos netname", "Neg netname"]}}, {"changed": {"name": "device config node", "object": "2s2p module/Terminal_T", "fields": ["Device position id"]}}]	51	1
483	2020-11-02 13:01:53.109177+00	18	Connector	2	[{"changed": {"fields": ["Abstract Specification"]}}]	61	1
484	2020-11-02 14:40:08.581201+00	19	Ivium_Cell1.txt	1	[{"added": {}}]	63	1
485	2020-11-02 14:44:55.813306+00	12	BioLogic_full.txt	1	[{"added": {}}]	23	1
486	2020-11-02 15:38:15.380898+00	8	BioLogic_full.txt	2	[]	23	1
487	2020-11-02 15:38:19.965418+00	12	BioLogic_full.txt	2	[]	23	1
488	2020-11-02 15:43:35.770424+00	12	BioLogic_full.txt	3		23	1
489	2020-11-02 15:43:47.259844+00	8	BioLogic_full.txt	3		23	1
490	2020-11-02 15:44:02.427224+00	5	mug.jpeg	3		23	1
491	2020-11-02 16:19:26.042091+00	2	Biologix	1	[{"added": {}}]	64	1
492	2020-11-02 16:19:31.170868+00	3	Novonix	1	[{"added": {}}]	64	1
493	2020-11-02 16:25:43.667774+00	4	Maccor	1	[{"added": {}}]	64	1
494	2020-11-02 16:26:03.385516+00	2	Biologic	2	[{"changed": {"fields": ["Name", "Module"]}}]	64	1
495	2020-11-02 16:31:11.965227+00	20	sample_Maccor.xlsx	1	[{"added": {}}]	63	1
496	2020-11-02 16:53:59.691844+00	21	sample_Maccor_2.xlsx	1	[{"added": {}}]	63	1
497	2020-11-02 17:02:54.675241+00	16	None	1	[{"added": {}}]	23	1
498	2020-11-02 18:07:10.766311+00	17	BioLogic_full.txt	1	[{"added": {}}]	23	1
499	2020-11-02 18:09:46.386673+00	17	BioLogic_full.txt	2	[{"changed": {"fields": ["Use parser"]}}]	23	1
500	2020-11-02 18:12:31.856469+00	17	BioLogic_full.txt	2	[]	23	1
501	2020-11-02 18:18:03.680101+00	17	BioLogic_full.txt	2	[{"changed": {"fields": ["Experiment"]}}]	23	1
502	2020-11-04 09:38:43.229821+00	1	My Folder	1	[{"added": {}}]	67	1
503	2020-11-04 09:38:58.362969+00	2	Another Folder	1	[{"added": {}}]	67	1
504	2020-11-04 11:58:58.791241+00	3	Equipment	1	[{"added": {}}]	11	1
505	2020-11-04 11:59:55.778816+00	8	cycler-foobar5000	1	[{"added": {}}]	12	1
506	2020-11-04 12:00:07.959583+00	8	cycler-foobar5000	2	[{"changed": {"fields": ["Groups"]}}]	12	1
507	2020-11-04 12:38:04.209464+00	19	Cycler Machine	1	[{"added": {}}]	61	1
508	2020-11-04 12:39:23.301945+00	20	Tom's GalvoTron 5000	1	[{"added": {}}]	61	1
509	2020-11-04 12:39:37.007503+00	1	GalvoTron 5000	1	[{"added": {}}]	65	1
510	2020-11-04 12:40:28.874625+00	1	None	1	[{"added": {}}]	68	1
511	2020-11-04 12:41:17.751425+00	8	c2fdceacffa198fd09d3f5baa7821b14f0ce0f22	1	[{"added": {}}]	46	1
512	2020-11-04 12:42:01.931545+00	1	None	2	[{"changed": {"fields": ["User token"]}}]	68	1
513	2020-11-05 15:32:25.278042+00	22	C_over_20_run_25_C_CA1.txt	1	[{"added": {}}]	63	1
514	2020-11-05 15:33:41.299393+00	18	C_over_20_run_25_C_CA1.txt	1	[{"added": {}}]	23	1
515	2020-11-05 15:52:58.068398+00	18	C_over_20_run_25_C_CA1.txt	2	[{"changed": {"fields": ["Use parser"]}}]	23	1
516	2020-11-05 15:54:20.632706+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
517	2020-11-05 15:55:18.539076+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
518	2020-11-05 15:55:49.317315+00	16	mug.jpeg	2	[{"changed": {"fields": ["Raw data file"]}}]	23	1
519	2020-11-10 14:33:34.34906+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
520	2020-11-10 14:35:34.558956+00	18	C_over_20_run_25_C_CA1.txt	2	[{"changed": {"fields": ["Use parser"]}}]	23	1
521	2020-11-10 15:18:25.989187+00	1	Biologix Most Fields	1	[{"added": {}}]	69	1
522	2020-11-11 17:50:31.800855+00	1	None	2	[{"changed": {"fields": ["User token"]}}]	68	1
523	2020-11-11 19:15:53.428366+00	1	makron	2	[{"changed": {"fields": ["Name"]}}]	68	1
524	2020-11-11 19:35:39.94558+00	2	foo	1	[{"added": {}}]	68	1
525	2020-11-11 19:35:54.924754+00	6	tom None 2020-11-10	2	[{"changed": {"fields": ["User owner"]}}]	8	1
526	2020-11-12 15:06:03.284494+00	5	tom My experiment 2020-11-01	2	[{"added": {"name": "experiment device", "object": "ExperimentDevice object (1)"}}]	8	1
527	2020-11-12 15:06:46.251925+00	5	tom My experiment 2020-11-01	2	[{"added": {"name": "experiment device", "object": "ExperimentDevice object (2)"}}]	8	1
528	2020-11-12 15:07:11.529124+00	5	tom My experiment 2020-11-01	2	[{"deleted": {"name": "experiment device", "object": "ExperimentDevice object (None)"}}]	8	1
529	2020-11-12 15:09:24.693747+00	5	tom My experiment 2020-11-01	2	[{"added": {"name": "experiment device", "object": "ExperimentDevice object (3)"}}, {"changed": {"name": "experiment device", "object": "ExperimentDevice object (1)", "fields": ["Data file"]}}]	8	1
530	2020-11-12 15:37:28.120471+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"changed": {"fields": ["Batch size"]}}]	38	1
531	2020-11-12 15:37:40.994553+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"added": {"name": "batch device", "object": "BatchDevice object (4)"}}]	38	1
532	2020-11-12 16:03:48.911082+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"deleted": {"name": "batch device", "object": "My NMC622 Cell/1"}}]	38	1
533	2020-11-12 16:04:02.131959+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"added": {"name": "batch device", "object": "My NMC622 Cell/4"}}]	38	1
534	2020-11-12 16:05:04.573034+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"added": {"name": "batch device", "object": "My NMC622 Cell/5"}}]	38	1
535	2020-11-12 16:05:12.916932+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"added": {"name": "batch device", "object": "My NMC622 Cell/6"}}]	38	1
536	2020-11-12 16:05:18.959289+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"deleted": {"name": "batch device", "object": "My NMC622 Cell/6"}}]	38	1
537	2020-11-12 16:21:03.55175+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"changed": {"name": "batch device", "object": "My NMC622 Cell/5", "fields": ["Notes"]}}]	38	1
538	2020-11-12 16:21:13.925727+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[]	38	1
539	2020-11-12 16:21:27.20621+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[]	38	1
540	2020-11-12 16:21:47.170005+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[]	38	1
541	2020-11-12 16:22:02.860423+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"changed": {"name": "batch device", "object": "My NMC622 Cell/3", "fields": ["Notes"]}}]	38	1
542	2020-11-12 16:50:19.716331+00	32	Imperial College My NMC622 Cell (5 off) 2020-11-01	2	[{"changed": {"fields": ["SerialNo"]}}]	38	1
543	2020-11-12 16:56:28.557557+00	21	Positive Electrode Material	1	[{"added": {}}, {"added": {"name": "device parameter", "object": "Thickness: t / m"}}]	61	1
544	2020-11-12 16:57:06.837317+00	9	Thickness: T / mm	1	[{"added": {}}]	32	1
545	2020-11-12 17:11:09.378166+00	6	LiPF6 (LiPF6)	1	[{"added": {}}]	28	1
546	2020-11-12 17:13:04.37283+00	2	Carbon (C)	2	[{"changed": {"fields": ["Mass"]}}]	28	1
549	2020-11-12 17:49:16.767023+00	1	NMC622	2	[{"added": {"name": "composition part", "object": "C1"}}]	29	1
550	2020-11-12 17:49:25.941192+00	1	NMC622	2	[{"deleted": {"name": "composition part", "object": "C1"}}]	29	1
551	2020-11-12 17:49:44.683192+00	21	Positive Electrode Material	2	[]	61	1
552	2020-11-12 18:01:07.037605+00	21	Positive Electrode Material	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
553	2020-11-12 18:01:12.856726+00	7	My NMC622 Cell	2	[{"changed": {"fields": ["parent", "lft", "rght", "tree_id", "level"]}}]	61	1
554	2020-11-12 18:02:22.079368+00	20	Tom's GalvoTron 5000	3		61	1
555	2020-11-12 18:06:23.409574+00	22	C_over_20_run_25_C_CA1.txt	2	[{"changed": {"fields": ["File"]}}]	63	1
556	2020-11-12 18:08:04.599891+00	10	Control Voltage: CV / V	1	[{"added": {}}]	32	1
557	2020-11-12 18:11:41.068051+00	1	Biologix Most Fields	2	[{"added": {"name": "signal type", "object": "SignalType object (1)"}}, {"added": {"name": "signal type", "object": "SignalType object (2)"}}, {"added": {"name": "signal type", "object": "SignalType object (3)"}}]	69	1
558	2020-11-12 18:12:50.949451+00	1	Biologix Most Fields	2	[{"changed": {"name": "signal type", "object": "SignalType object (1)", "fields": ["Order"]}}]	69	1
559	2020-11-12 18:13:00.071757+00	1	Biologix Most Fields	2	[{"changed": {"name": "signal type", "object": "SignalType object (3)", "fields": ["Order"]}}]	69	1
560	2020-11-12 19:55:14.890199+00	13	Time (s) / s	1	[{"added": {}}]	31	1
561	2020-11-12 19:55:19.684234+00	11	Time: t / s	1	[{"added": {}}]	32	1
562	2020-11-12 19:56:33.084759+00	14	int (.) / x	1	[{"added": {}}]	31	1
563	2020-11-12 19:56:45.386903+00	12	Sample nu,ber: x / x	1	[{"added": {}}]	32	1
564	2020-11-12 19:56:56.625176+00	12	Sample number: x / x	2	[{"changed": {"fields": ["Name"]}}]	32	1
565	2020-11-12 20:22:19.396428+00	1	Biologix Most Fields	2	[{"added": {"name": "signal type", "object": "SignalType object (4)"}}]	69	1
566	2020-11-12 21:10:51.074785+00	4	Pack	2	[{"changed": {"fields": ["Attributes"]}}]	61	1
567	2020-11-12 21:11:42.420412+00	5	Module	2	[{"changed": {"fields": ["Attributes"]}}]	61	1
568	2020-11-12 21:24:14.810051+00	5	Module	2	[{"changed": {"fields": ["Inherit metadata attributes from parent"]}}]	61	1
569	2020-11-12 21:24:48.553184+00	5	Module	2	[{"changed": {"fields": ["Attributes"]}}]	61	1
570	2020-11-12 21:25:13.935469+00	4	Pack	2	[{"changed": {"fields": ["Attributes"]}}]	61	1
571	2020-11-13 11:08:45.126751+00	18	C_over_20_run_25_C_CA1.txt	2	[{"changed": {"fields": ["Use parser"]}}]	23	1
572	2020-11-13 11:09:39.970707+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
573	2020-11-13 11:11:44.955647+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
574	2020-11-13 11:18:43.16962+00	17	BioLogic_full.txt	2	[{"changed": {"fields": ["Use parser"]}}]	23	1
575	2020-11-13 12:23:31.070938+00	17	BioLogic_full.txt	2	[]	23	1
576	2020-11-13 12:53:30.409536+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
577	2020-11-13 13:39:42.702542+00	17	BioLogic_full.txt	2	[]	23	1
578	2020-11-13 13:55:50.957282+00	1	Biologix Most Fields	2	[{"changed": {"name": "signal type", "object": "SignalType object (2)", "fields": ["Order"]}}, {"changed": {"name": "signal type", "object": "SignalType object (3)", "fields": ["Order"]}}, {"changed": {"name": "signal type", "object": "SignalType object (4)", "fields": ["Order"]}}]	69	1
579	2020-11-13 13:56:03.561772+00	1	Biologix Default Fields	2	[{"changed": {"fields": ["Name"]}}]	69	1
580	2020-11-13 13:58:43.411891+00	1	Biologix Default Fields	2	[]	69	1
581	2020-11-13 13:58:51.885162+00	17	BioLogic_full.txt	2	[]	23	1
582	2020-11-13 13:59:12.211349+00	17	BioLogic_full.txt	2	[]	23	1
583	2020-11-13 14:02:10.785002+00	17	BioLogic_full.txt	2	[]	23	1
584	2020-11-13 14:02:32.238534+00	1	Biologix Default Fields	2	[{"changed": {"name": "signal type", "object": "Time", "fields": ["Col name"]}}]	69	1
585	2020-11-13 14:02:40.787254+00	17	BioLogic_full.txt	2	[]	23	1
586	2020-11-13 14:03:44.77385+00	17	BioLogic_full.txt	2	[]	23	1
587	2020-11-13 14:31:41.927706+00	17	BioLogic_full.txt	2	[]	23	1
588	2020-11-13 14:31:53.168201+00	17	BioLogic_full.txt	2	[]	23	1
589	2020-11-13 14:32:13.313832+00	17	BioLogic_full.txt	2	[{"changed": {"name": "data range", "object": "BioLogic_full.txt/16: all", "fields": ["File offset start", "File offset end"]}}]	23	1
590	2020-11-13 14:33:02.980564+00	17	BioLogic_full.txt	2	[{"changed": {"name": "data range", "object": "BioLogic_full.txt/16: all", "fields": ["File offset start", "File offset end"]}}]	23	1
591	2020-11-13 14:35:07.449224+00	17	BioLogic_full.txt	2	[{"added": {"name": "data range", "object": "BioLogic_full.txt/17: foo"}}, {"changed": {"name": "data range", "object": "BioLogic_full.txt/16: all", "fields": ["File offset start", "File offset end"]}}]	23	1
592	2020-11-13 14:35:40.081739+00	17	BioLogic_full.txt	2	[{"changed": {"name": "data range", "object": "BioLogic_full.txt/16: all", "fields": ["File offset start", "File offset end", "Step action"]}}]	23	1
593	2020-11-13 14:38:25.321212+00	17	BioLogic_full.txt	2	[{"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: all"}}]	23	1
594	2020-11-13 14:38:38.890567+00	17	BioLogic_full.txt	2	[{"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: foo"}}]	23	1
595	2020-11-13 14:39:41.518761+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
596	2020-11-13 14:41:09.721625+00	17	BioLogic_full.txt	2	[{"changed": {"name": "data range", "object": "BioLogic_full.txt/18: all", "fields": ["Ts headers"]}}]	23	1
597	2020-11-13 14:41:20.816504+00	17	BioLogic_full.txt	2	[{"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: all"}}]	23	1
598	2020-11-13 14:41:26.740081+00	17	BioLogic_full.txt	2	[]	23	1
599	2020-11-13 14:49:07.850374+00	17	BioLogic_full.txt	2	[]	23	1
600	2020-11-13 14:49:55.298277+00	17	BioLogic_full.txt	2	[{"changed": {"name": "data range", "object": "BioLogic_full.txt/20: all", "fields": ["Ts data"]}}]	23	1
601	2020-11-13 14:50:09.240268+00	17	BioLogic_full.txt	2	[{"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: all"}}]	23	1
602	2020-11-13 14:50:13.009482+00	17	BioLogic_full.txt	2	[]	23	1
603	2020-11-13 14:51:49.990756+00	17	BioLogic_full.txt	2	[{"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: all"}}]	23	1
604	2020-11-13 14:51:53.948067+00	17	BioLogic_full.txt	2	[]	23	1
605	2020-11-13 15:34:23.901229+00	17	BioLogic_full.txt	2	[{"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: all"}}]	23	1
606	2020-11-13 15:38:07.213984+00	17	BioLogic_full.txt	2	[{"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: Time"}}, {"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: Ecell/V"}}, {"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: I/mA"}}, {"deleted": {"name": "data range", "object": "BioLogic_full.txt/0: control/V"}}]	23	1
607	2020-11-13 16:10:27.038002+00	1	Biologix V,I,CV	2	[{"changed": {"fields": ["Name"]}}]	69	1
608	2020-11-13 16:10:41.673647+00	2	Biologix Default	1	[{"added": {}}, {"added": {"name": "signal type", "object": "Time"}}, {"added": {"name": "signal type", "object": "Ecell/V"}}, {"added": {"name": "signal type", "object": "I/mA"}}, {"added": {"name": "signal type", "object": "control/V"}}]	69	1
609	2020-11-13 16:11:03.189822+00	1	Biologix V,I,CV	2	[{"deleted": {"name": "signal type", "object": "Time"}}]	69	1
610	2020-11-13 16:11:53.769596+00	17	BioLogic_full.txt	2	[]	23	1
611	2020-11-13 16:12:13.736847+00	17	BioLogic_full.txt	2	[{"changed": {"fields": ["Use parser"]}}]	23	1
612	2020-11-13 16:13:48.23214+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
613	2020-11-13 16:36:40.910362+00	18	C_over_20_run_25_C_CA1.txt	2	[]	23	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: towen
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
8	battDB	experiment
10	auth	permission
11	auth	group
12	auth	user
13	contenttypes	contenttype
14	admin	logentry
15	sessions	session
22	battDB	datarange
23	battDB	experimentdatafile
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
38	battDB	devicebatch
45	authtoken	token
46	authtoken	tokenproxy
48	dfndb	dataparameter
50	battDB	deviceconfignode
51	battDB	deviceconfig
57	battDB	batchdevice
60	battDB	datacolumn
61	battDB	devicespecification
62	battDB	deviceparameter
63	common	uploadedfile
64	battDB	dataparser
65	battDB	equipment
66	battDB	folder
67	battDB	filefolder
68	battDB	harvester
69	battDB	parser
70	battDB	signaltype
71	battDB	experimentdevice
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
166	battDB	0077_auto_20201019_1520	2020-10-19 16:24:44.746874+01
167	common	0027_auto_20201019_1515	2020-10-19 16:24:44.801455+01
168	common	0028_remove_paper_slug	2020-10-19 16:24:44.817054+01
169	dfndb	0031_auto_20201019_1515	2020-10-19 16:24:44.871755+01
170	common	0029_paper_slug	2020-10-19 16:59:00.007833+01
171	dfndb	0032_auto_20201020_0903	2020-10-20 10:03:39.742447+01
172	battDB	0078_auto_20201020_0903	2020-10-20 10:03:39.925265+01
173	battDB	0079_auto_20201020_0919	2020-10-20 10:19:51.028859+01
174	battDB	0080_auto_20201020_1000	2020-10-20 11:01:25.721509+01
175	battDB	0081_auto_20201020_1018	2020-10-20 11:18:29.38124+01
176	battDB	0082_auto_20201021_1112	2020-10-21 12:12:44.491812+01
177	common	0030_auto_20201021_1112	2020-10-21 12:12:44.508888+01
178	dfndb	0033_auto_20201021_1112	2020-10-21 12:12:44.570172+01
179	battDB	0083_device_serialno	2020-10-21 12:23:17.941164+01
180	battDB	0084_device_manufacturer	2020-10-21 12:34:06.887883+01
181	common	0031_auto_20201021_1138	2020-10-21 12:38:47.060591+01
182	battDB	0085_auto_20201021_1223	2020-10-21 13:23:49.282414+01
183	battDB	0086_auto_20201022_1030	2020-10-22 11:30:23.510595+01
184	battDB	0087_deviceconfignode_device_position_id	2020-10-22 11:42:50.675115+01
185	battDB	0088_auto_20201022_1153	2020-10-22 12:53:45.740454+01
186	battDB	0089_auto_20201022_1507	2020-10-22 16:07:42.081004+01
187	battDB	0090_auto_20201022_1946	2020-10-22 20:46:30.638996+01
188	battDB	0091_auto_20201022_1947	2020-10-22 20:47:21.499028+01
189	battDB	0092_auto_20201022_2335	2020-10-23 00:35:53.164347+01
190	battDB	0093_auto_20201026_1141	2020-10-26 11:41:25.56533+00
191	battDB	0094_auto_20201026_1208	2020-10-26 12:08:40.147447+00
192	battDB	0095_auto_20201026_1245	2020-10-26 12:45:44.600734+00
193	common	0032_auto_20201026_1245	2020-10-26 12:45:44.629801+00
194	common	0033_auto_20201026_1247	2020-10-26 12:47:36.367464+00
195	common	0034_compositeThing	2020-10-26 13:18:40.712358+00
196	common	0035_ThingParts	2020-10-26 13:46:54.487556+00
197	common	0036_MPTT_Thing	2020-10-26 14:11:14.42603+00
198	common	0037_auto_20201026_1412	2020-10-26 14:12:40.08033+00
199	common	0038_MPTT_Thing_parent	2020-10-26 15:06:01.616118+00
200	common	0039_MPTT_Thing_parent_revert	2020-10-26 16:24:58.625979+00
201	common	0040_MPTT_Thing_parent_rev2	2020-10-26 16:27:07.522374+00
202	common	0041_auto_20201026_1631	2020-10-26 16:31:48.771737+00
203	common	0042_delete_thing	2020-10-26 16:45:57.195778+00
204	common	0043_MPTT_Thing	2020-10-26 19:38:59.692641+00
205	battDB	0096_MPTT_Thing	2020-10-26 19:43:44.633397+00
206	common	0044_MPTT_Device	2020-10-26 23:58:22.953496+00
207	battDB	0097_MPTT_Device	2020-10-26 23:58:23.071609+00
208	common	0045_auto_20201027_0000	2020-10-27 00:01:05.343021+00
209	battDB	0098_auto_20201027_0021	2020-10-27 00:21:26.079973+00
210	common	0046_auto_20201027_0021	2020-10-27 00:21:26.114116+00
211	battDB	0099_experimentThing	2020-10-27 11:01:54.227306+00
212	battDB	0100_BatchDevice	2020-10-27 12:20:11.236466+00
213	battDB	0101_BatchDeviceAttributes	2020-10-27 12:21:23.899276+00
214	battDB	0102_device_specification	2020-10-28 11:13:00.306127+00
215	common	0047_auto_20201028_1112	2020-10-28 11:13:00.331548+00
216	battDB	0103_auto_20201028_1135	2020-10-28 11:35:38.103046+00
217	battDB	0104_auto_20201028_1225	2020-10-28 12:25:17.30317+00
218	battDB	0105_DeleteDeviceConfig	2020-10-28 12:59:57.679599+00
219	battDB	0106_ReinstateDataFile	2020-10-28 13:53:41.091433+00
220	battDB	0107_ExperimentNotAThing	2020-10-28 14:12:28.00095+00
221	battDB	0108_ExperimentNotAThin	2020-10-28 14:18:16.298121+00
222	battDB	0109_DeviceData	2020-10-28 14:41:50.725582+00
223	battDB	0110_auto_20201028_1504	2020-10-28 15:04:30.825652+00
224	battDB	0111_auto_20201028_1537	2020-10-28 15:37:10.42883+00
225	battDB	0112_experimentdatafile_parsed_data	2020-10-28 15:43:30.352171+00
226	battDB	0113_auto_20201028_1543	2020-10-28 15:43:30.377546+00
227	battDB	0114_DataColumn	2020-10-28 15:55:21.086139+00
228	battDB	0115_DataColumnBork	2020-10-28 15:55:21.126087+00
229	battDB	0116_DataColumnBork	2020-10-28 15:57:45.354853+00
230	battDB	0117_DeviceSpecificationBatch	2020-10-29 12:01:11.409193+00
231	battDB	0118_DeviceParameter	2020-10-29 12:33:36.178607+00
232	battDB	0119_DeviceBatch	2020-10-29 14:15:27.818347+00
233	battDB	0120_DeviceConfig	2020-10-30 10:35:06.1684+00
234	battDB	0121_Docstrings	2020-10-30 10:49:03.977378+00
235	common	0048_Docstrings	2020-10-30 10:49:04.002475+00
236	dfndb	0034_Docstrings	2020-10-30 10:49:04.066066+00
237	battDB	0122_AbstractSpec	2020-10-30 10:56:21.338558+00
238	battDB	0123_DeviceSpecType	2020-10-30 11:37:00.525607+00
239	battDB	0124_DeviceSpecType	2020-10-30 11:43:39.92622+00
240	battDB	0125_DeviceParamName	2020-10-30 12:05:03.342441+00
241	battDB	0126_DeviceParamSpec	2020-10-30 12:09:15.701083+00
242	dfndb	0035_ParamMeta	2020-10-30 12:16:58.876171+00
243	battDB	0127_auto_20201030_1423	2020-10-30 14:23:24.168509+00
244	battDB	0128_auto_20201030_1453	2020-10-30 14:53:43.035331+00
245	battDB	0129_devicespecification_complete	2020-10-30 14:55:45.698764+00
246	battDB	0130_auto_20201030_1457	2020-10-30 14:57:39.455306+00
247	battDB	0131_Bork	2020-10-31 16:24:47.91541+00
248	common	0049_Bork	2020-10-31 16:24:47.92398+00
249	battDB	0132_Bork	2020-10-31 16:24:47.932202+00
250	battDB	0133_RecreateAllModels	2020-10-31 16:25:33.26896+00
251	common	0050_ExperimentDataFile	2020-11-01 13:38:07.89016+00
252	battDB	0134_ExperimentDataFile	2020-11-01 13:38:08.033279+00
253	battDB	0135_DataColumn	2020-11-01 14:38:27.667945+00
254	battDB	0136_SlugFieldMaxLen500	2020-11-01 15:08:16.471882+00
255	common	0051_SlugFieldMaxLen500	2020-11-01 15:08:16.505644+00
256	dfndb	0036_SlugFieldMaxLen500	2020-11-01 15:08:16.61404+00
257	battDB	0137_auto_20201101_1652	2020-11-01 16:53:02.334671+00
259	battDB	0138_deviceparameter_inherit_to_children	2020-11-01 17:26:26.133797+00
260	battDB	0139_auto_20201101_1739	2020-11-01 17:39:42.081405+00
261	battDB	0140_remove_devicebatch_name	2020-11-01 17:41:23.088967+00
262	battDB	0141_remove_experiment_device	2020-11-01 17:42:52.170147+00
263	battDB	0142_DataParser	2020-11-02 10:26:14.548775+00
264	battDB	0143_dataparser_module	2020-11-02 10:42:03.985212+00
265	battDB	0144_experimentDataMetadata	2020-11-02 11:04:51.006601+00
266	battDB	0145_experiment_config	2020-11-02 11:46:37.729243+00
267	battDB	0146_DeviceConfigNetNames	2020-11-02 12:31:13.891521+00
268	battDB	0147_DataEquipment	2020-11-02 14:43:27.559735+00
269	battDB	0148_auto_20201102_1552	2020-11-02 15:53:04.101124+00
270	common	0052_auto_20201102_1552	2020-11-02 15:53:04.149477+00
271	battDB	0149_DataParser_No_BaseModel	2020-11-02 16:19:23.59724+00
272	battDB	0150_dataparser_notes	2020-11-02 16:20:04.637337+00
273	battDB	0151_auto_20201102_1621	2020-11-02 16:21:41.149622+00
274	battDB	0152_auto_20201102_1733	2020-11-02 17:33:17.609604+00
275	battDB	0153_experimentdatafile_use_parser	2020-11-02 17:33:28.126313+00
276	dfndb	0037_ManufacturingProtocol	2020-11-03 15:46:45.145427+00
277	battDB	0154_ManufacturingProtocol	2020-11-03 15:46:45.202334+00
279	battDB	0155_FileFolder	2020-11-04 09:37:42.759265+00
280	battDB	0156_Harvester	2020-11-04 12:35:42.037459+00
281	battDB	0157_ParserSignal	2020-11-10 15:01:20.953068+00
282	battDB	0158_experimentdatafile_use_parser	2020-11-10 15:03:17.703598+00
283	battDB	0159_ParserBaseModel	2020-11-10 15:12:11.921606+00
284	battDB	0160_remove_harvester_user_token	2020-11-11 19:03:11.118508+00
285	battDB	0161_BaseModelMandatoryName	2020-11-11 19:07:41.345532+00
286	battDB	0162_auto_20201111_1911	2020-11-11 19:11:27.521015+00
287	battDB	0163_ts_notnull	2020-11-12 11:45:06.309729+00
288	battDB	0164_deviceconfig_config_type	2020-11-12 11:45:06.340941+00
289	battDB	0165_auto_20201112_1220	2020-11-12 12:20:53.94758+00
290	battDB	0166_ExperimentFileFolder	2020-11-12 12:33:04.071707+00
291	battDB	0167_DataRangeType	2020-11-12 12:44:45.913063+00
292	battDB	0168_DataColumn	2020-11-12 13:46:52.671035+00
294	battDB	0169_ExperimentDevice	2020-11-12 15:00:12.957083+00
295	battDB	0170_delete_datacolumn	2020-11-12 15:03:27.325387+00
296	battDB	0171_datacolumn	2020-11-12 15:03:53.462883+00
297	battDB	0172_auto_20201112_1505	2020-11-12 15:05:41.331559+00
298	battDB	0173_auto_20201112_1511	2020-11-12 15:11:26.092498+00
299	battDB	0174_auto_20201112_1519	2020-11-12 15:30:19.806095+00
300	battDB	0175_auto_20201112_1520	2020-11-12 15:30:19.84965+00
301	battDB	0176_BatchDevice	2020-11-12 15:30:19.892175+00
302	battDB	0177_batchdevice_notes	2020-11-12 15:39:21.690796+00
303	battDB	0178_auto_20201112_1603	2020-11-12 16:03:26.194017+00
304	battDB	0179_auto_20201112_1710	2020-11-12 17:10:57.734199+00
305	dfndb	0038_auto_20201112_1710	2020-11-12 17:10:57.782375+00
306	dfndb	0039_auto_20201112_1751	2020-11-12 17:51:16.652868+00
307	battDB	0180_remove_harvester_upload_to_folder	2020-11-12 17:57:57.033467+00
308	battDB	0181_auto_20201112_1803	2020-11-12 18:03:08.450768+00
309	battDB	0182_signaltype_order	2020-11-12 18:11:19.526627+00
310	battDB	0183_auto_20201112_2034	2020-11-12 20:39:16.044952+00
311	battDB	0184_devicespecification_inherit_metadata	2020-11-12 21:07:18.16946+00
312	battDB	0185_auto_20201112_2108	2020-11-12 21:08:27.326171+00
313	battDB	0186_auto_20201113_1317	2020-11-13 13:17:28.028834+00
314	battDB	0187_dataRange	2020-11-13 14:34:46.152886+00
315	battDB	0188_dataRange	2020-11-13 16:19:32.608776+00
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
i50nfgp0d9lr4o4xa9r7n38hn3b3flsf	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kXMfF:FCILVNS4TYGSwjZqVzGQbwp-d-b-Ho3DlZcdH3VE0gA	2020-11-10 10:57:17.43594+00
hbds84guogxhc8o1p9e0dbsn0479ehso	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kZamI:X67Jb2pGIuLroN5p8YY4sk19hN7DH5S-QP4Btp8tvsM	2020-11-16 14:25:46.306248+00
pwreojo0dmcrbpv0ueeaxrlb0bn6j3r3	.eJxVjEEOwiAQRe_C2hCo0AGX7j0DYZhBqgaS0q6Md7dNutDte-__twhxXUpYO89hInERWpx-Gcb05LoLesR6bzK1uswTyj2Rh-3y1ohf16P9Oyixl22dCX0yRiftFDuA0TEyD-MZVWZvrQPMoAZvDJDXeiOaHKgMLloEAvH5AuGMN2w:1kcSOs:pKtvvkl9Vor8Mf1D3jhgsWiaO_HP-rLt4xlg3Xf5BRk	2020-11-24 12:05:26.636338+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 3, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 169, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 284, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 2, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 8, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 104, true);


--
-- Name: battDB_batchdevice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_batchdevice_id_seq"', 8, true);


--
-- Name: battDB_datacolumn_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_datacolumn_id_seq"', 1, false);


--
-- Name: battDB_devicebatch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_devicebatch_id_seq"', 32, true);


--
-- Name: battDB_deviceconfig_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_deviceconfig_id_seq"', 4, true);


--
-- Name: battDB_deviceconfignode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_deviceconfignode_id_seq"', 16, true);


--
-- Name: battDB_deviceparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_deviceparameter_id_seq"', 4, true);


--
-- Name: battDB_devicespecification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_devicespecification_id_seq"', 21, true);


--
-- Name: battDB_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_equipment_id_seq"', 1, true);


--
-- Name: battDB_experiment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_experiment_id_seq"', 8, true);


--
-- Name: battDB_experimentdatafile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_experimentdatafile_id_seq"', 18, true);


--
-- Name: battDB_experimentdevice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_experimentdevice_id_seq"', 3, true);


--
-- Name: battDB_filefolder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_filefolder_id_seq"', 2, true);


--
-- Name: battDB_harvester_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_harvester_id_seq"', 2, true);


--
-- Name: battDB_parser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_parser_id_seq"', 2, true);


--
-- Name: battDB_signaltype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public."battDB_signaltype_id_seq"', 8, true);


--
-- Name: common_org_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_org_id_seq', 2, true);


--
-- Name: common_paper_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_paper_id_seq', 2, true);


--
-- Name: common_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_person_id_seq', 2, true);


--
-- Name: common_uploadedfile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.common_uploadedfile_id_seq', 22, true);


--
-- Name: dfndb_compositionpart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_compositionpart_id_seq', 7, true);


--
-- Name: dfndb_compound_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_compound_id_seq', 6, true);


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

SELECT pg_catalog.setval('public.dfndb_method_id_seq', 4, true);


--
-- Name: dfndb_parameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_parameter_id_seq', 12, true);


--
-- Name: dfndb_quantityunit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.dfndb_quantityunit_id_seq', 14, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 613, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 71, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: towen
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 315, true);


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
-- Name: battDB_batchdevice battDB_batchdevice_batch_id_seq_num_d6b32856_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_batchdevice"
    ADD CONSTRAINT "battDB_batchdevice_batch_id_seq_num_d6b32856_uniq" UNIQUE (batch_id, seq_num);


--
-- Name: battDB_batchdevice battDB_batchdevice_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_batchdevice"
    ADD CONSTRAINT "battDB_batchdevice_pkey" PRIMARY KEY (id);


--
-- Name: battDB_datacolumn battDB_datacolumn_column_name_data_file_id_8f143447_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datacolumn"
    ADD CONSTRAINT "battDB_datacolumn_column_name_data_file_id_8f143447_uniq" UNIQUE (column_name, data_file_id);


--
-- Name: battDB_datacolumn battDB_datacolumn_device_id_data_file_id_86f54ef0_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datacolumn"
    ADD CONSTRAINT "battDB_datacolumn_device_id_data_file_id_86f54ef0_uniq" UNIQUE (device_id, data_file_id);


--
-- Name: battDB_datacolumn battDB_datacolumn_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datacolumn"
    ADD CONSTRAINT "battDB_datacolumn_pkey" PRIMARY KEY (id);


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
-- Name: battDB_deviceparameter battDB_deviceparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceparameter"
    ADD CONSTRAINT "battDB_deviceparameter_pkey" PRIMARY KEY (id);


--
-- Name: battDB_deviceparameter battDB_deviceparameter_spec_id_name_573d8260_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceparameter"
    ADD CONSTRAINT "battDB_deviceparameter_spec_id_name_573d8260_uniq" UNIQUE (spec_id, name);


--
-- Name: battDB_deviceparameter battDB_deviceparameter_spec_id_parameter_id_mat_d5022058_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceparameter"
    ADD CONSTRAINT "battDB_deviceparameter_spec_id_parameter_id_mat_d5022058_uniq" UNIQUE (spec_id, parameter_id, material_id);


--
-- Name: battDB_devicespecification battDB_devicespecification_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicespecification"
    ADD CONSTRAINT "battDB_devicespecification_pkey" PRIMARY KEY (id);


--
-- Name: battDB_equipment battDB_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experiment battDB_experiment_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experimentdatafile battDB_experimentdatafil_raw_data_file_id_experim_241d6d9d_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdatafil_raw_data_file_id_experim_241d6d9d_uniq" UNIQUE (raw_data_file_id, experiment_id);


--
-- Name: battDB_experimentdatafile battDB_experimentdatafile_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdatafile_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experimentdevice battDB_experimentdevice_device_pos_data_file_id_419c3bbc_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdevice"
    ADD CONSTRAINT "battDB_experimentdevice_device_pos_data_file_id_419c3bbc_uniq" UNIQUE (device_pos, data_file_id);


--
-- Name: battDB_experimentdevice battDB_experimentdevice_experiment_id_device_id__2fcaf74c_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdevice"
    ADD CONSTRAINT "battDB_experimentdevice_experiment_id_device_id__2fcaf74c_uniq" UNIQUE (experiment_id, "deviceBatch_id", batch_seq, data_file_id);


--
-- Name: battDB_experimentdevice battDB_experimentdevice_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdevice"
    ADD CONSTRAINT "battDB_experimentdevice_pkey" PRIMARY KEY (id);


--
-- Name: battDB_filefolder battDB_filefolder_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_filefolder"
    ADD CONSTRAINT "battDB_filefolder_pkey" PRIMARY KEY (id);


--
-- Name: battDB_harvester battDB_harvester_name_user_owner_id_0b314229_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_harvester"
    ADD CONSTRAINT "battDB_harvester_name_user_owner_id_0b314229_uniq" UNIQUE (name, user_owner_id);


--
-- Name: battDB_harvester battDB_harvester_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_harvester"
    ADD CONSTRAINT "battDB_harvester_pkey" PRIMARY KEY (id);


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
-- Name: battDB_parser battDB_parser_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_parser"
    ADD CONSTRAINT "battDB_parser_pkey" PRIMARY KEY (id);


--
-- Name: battDB_signaltype battDB_signaltype_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_signaltype"
    ADD CONSTRAINT "battDB_signaltype_pkey" PRIMARY KEY (id);


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
-- Name: common_uploadedfile common_uploadedfile_hash_key; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_uploadedfile
    ADD CONSTRAINT common_uploadedfile_hash_key UNIQUE (hash);


--
-- Name: common_uploadedfile common_uploadedfile_pkey; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_uploadedfile
    ADD CONSTRAINT common_uploadedfile_pkey PRIMARY KEY (id);


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
-- Name: dfndb_parameter dfndb_parameter_symbol_unit_id_0999db25_uniq; Type: CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.dfndb_parameter
    ADD CONSTRAINT dfndb_parameter_symbol_unit_id_0999db25_uniq UNIQUE (symbol, unit_id);


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
-- Name: battDB_batchdevice_batch_id_8cefc0b1; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_batchdevice_batch_id_8cefc0b1" ON public."battDB_batchdevice" USING btree (batch_id);


--
-- Name: battDB_datacolumn_data_file_id_df73df9e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_datacolumn_data_file_id_df73df9e" ON public."battDB_datacolumn" USING btree (data_file_id);


--
-- Name: battDB_datacolumn_device_id_bee39a70; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_datacolumn_device_id_bee39a70" ON public."battDB_datacolumn" USING btree (device_id);


--
-- Name: battDB_datacolumn_parameter_id_1d518565; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_datacolumn_parameter_id_1d518565" ON public."battDB_datacolumn" USING btree (parameter_id);


--
-- Name: battDB_devicebatch_manufacturer_id_85675f1a; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_manufacturer_id_85675f1a" ON public."battDB_devicebatch" USING btree (manufacturer_id);


--
-- Name: battDB_devicebatch_manufacturing_protocol_id_0ffaa425; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_manufacturing_protocol_id_0ffaa425" ON public."battDB_devicebatch" USING btree (manufacturing_protocol_id);


--
-- Name: battDB_devicebatch_parent_id_e0be7099; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_parent_id_e0be7099" ON public."battDB_devicebatch" USING btree (parent_id);


--
-- Name: battDB_devicebatch_slug_d40e4daa; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_slug_d40e4daa" ON public."battDB_devicebatch" USING btree (slug);


--
-- Name: battDB_devicebatch_slug_d40e4daa_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_slug_d40e4daa_like" ON public."battDB_devicebatch" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_devicebatch_specification_id_528663e7; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_specification_id_528663e7" ON public."battDB_devicebatch" USING btree (specification_id);


--
-- Name: battDB_devicebatch_tree_id_7c72ce78; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_tree_id_7c72ce78" ON public."battDB_devicebatch" USING btree (tree_id);


--
-- Name: battDB_devicebatch_user_owner_id_a17097e8; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicebatch_user_owner_id_a17097e8" ON public."battDB_devicebatch" USING btree (user_owner_id);


--
-- Name: battDB_deviceconfig_slug_eede7fcb; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfig_slug_eede7fcb" ON public."battDB_deviceconfig" USING btree (slug);


--
-- Name: battDB_deviceconfig_slug_eede7fcb_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfig_slug_eede7fcb_like" ON public."battDB_deviceconfig" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_deviceconfig_user_owner_id_9f82fb32; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfig_user_owner_id_9f82fb32" ON public."battDB_deviceconfig" USING btree (user_owner_id);


--
-- Name: battDB_deviceconfignode_config_id_08206ff9; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfignode_config_id_08206ff9" ON public."battDB_deviceconfignode" USING btree (config_id);


--
-- Name: battDB_deviceconfignode_device_id_21bed58f; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceconfignode_device_id_21bed58f" ON public."battDB_deviceconfignode" USING btree (device_id);


--
-- Name: battDB_deviceparameter_material_id_0e7af7bd; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceparameter_material_id_0e7af7bd" ON public."battDB_deviceparameter" USING btree (material_id);


--
-- Name: battDB_deviceparameter_parameter_id_5107f443; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceparameter_parameter_id_5107f443" ON public."battDB_deviceparameter" USING btree (parameter_id);


--
-- Name: battDB_deviceparameter_spec_id_5c622dac; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_deviceparameter_spec_id_5c622dac" ON public."battDB_deviceparameter" USING btree (spec_id);


--
-- Name: battDB_devicespecification_device_type_id_81af892f; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicespecification_device_type_id_81af892f" ON public."battDB_devicespecification" USING btree (device_type_id);


--
-- Name: battDB_devicespecification_parent_id_5f4c7c57; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicespecification_parent_id_5f4c7c57" ON public."battDB_devicespecification" USING btree (parent_id);


--
-- Name: battDB_devicespecification_slug_cc327c86; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicespecification_slug_cc327c86" ON public."battDB_devicespecification" USING btree (slug);


--
-- Name: battDB_devicespecification_slug_cc327c86_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicespecification_slug_cc327c86_like" ON public."battDB_devicespecification" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_devicespecification_tree_id_d687d194; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicespecification_tree_id_d687d194" ON public."battDB_devicespecification" USING btree (tree_id);


--
-- Name: battDB_devicespecification_user_owner_id_35f6fdb1; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_devicespecification_user_owner_id_35f6fdb1" ON public."battDB_devicespecification" USING btree (user_owner_id);


--
-- Name: battDB_equipment_default_parser_id_d9728b28; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_default_parser_id_d9728b28" ON public."battDB_equipment" USING btree (default_parser_id);


--
-- Name: battDB_equipment_manufacturer_id_52eef8ee; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_manufacturer_id_52eef8ee" ON public."battDB_equipment" USING btree (manufacturer_id);


--
-- Name: battDB_equipment_slug_c2223721; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_slug_c2223721" ON public."battDB_equipment" USING btree (slug);


--
-- Name: battDB_equipment_slug_c2223721_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_slug_c2223721_like" ON public."battDB_equipment" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_equipment_specification_id_cae1bbf7; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_specification_id_cae1bbf7" ON public."battDB_equipment" USING btree (specification_id);


--
-- Name: battDB_equipment_user_owner_id_bbb9f49e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_equipment_user_owner_id_bbb9f49e" ON public."battDB_equipment" USING btree (user_owner_id);


--
-- Name: battDB_experiment_config_id_308e8e11; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_config_id_308e8e11" ON public."battDB_experiment" USING btree (config_id);


--
-- Name: battDB_experiment_folder_id_ffc45c6a; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_folder_id_ffc45c6a" ON public."battDB_experiment" USING btree (folder_id);


--
-- Name: battDB_experiment_protocol_id_ed0e9fcd; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_protocol_id_ed0e9fcd" ON public."battDB_experiment" USING btree (protocol_id);


--
-- Name: battDB_experiment_slug_392e85c7; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_slug_392e85c7" ON public."battDB_experiment" USING btree (slug);


--
-- Name: battDB_experiment_slug_392e85c7_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_slug_392e85c7_like" ON public."battDB_experiment" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_experiment_user_owner_id_3a1061fa; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experiment_user_owner_id_3a1061fa" ON public."battDB_experiment" USING btree (user_owner_id);


--
-- Name: battDB_experimentdatafile_experiment_id_de169b40; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_experiment_id_de169b40" ON public."battDB_experimentdatafile" USING btree (experiment_id);


--
-- Name: battDB_experimentdatafile_machine_id_383367b5; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_machine_id_383367b5" ON public."battDB_experimentdatafile" USING btree (machine_id);


--
-- Name: battDB_experimentdatafile_raw_data_file_id_91752398; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_raw_data_file_id_91752398" ON public."battDB_experimentdatafile" USING btree (raw_data_file_id);


--
-- Name: battDB_experimentdatafile_slug_3950aa51; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_slug_3950aa51" ON public."battDB_experimentdatafile" USING btree (slug);


--
-- Name: battDB_experimentdatafile_slug_3950aa51_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_slug_3950aa51_like" ON public."battDB_experimentdatafile" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_experimentdatafile_use_parser_id_fffb2715; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_use_parser_id_fffb2715" ON public."battDB_experimentdatafile" USING btree (use_parser_id);


--
-- Name: battDB_experimentdatafile_user_owner_id_f8f951f2; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdatafile_user_owner_id_f8f951f2" ON public."battDB_experimentdatafile" USING btree (user_owner_id);


--
-- Name: battDB_experimentdevice_data_file_id_1a1175e3; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdevice_data_file_id_1a1175e3" ON public."battDB_experimentdevice" USING btree (data_file_id);


--
-- Name: battDB_experimentdevice_device_id_c2d32af9; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdevice_device_id_c2d32af9" ON public."battDB_experimentdevice" USING btree ("deviceBatch_id");


--
-- Name: battDB_experimentdevice_experiment_id_566fbea4; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_experimentdevice_experiment_id_566fbea4" ON public."battDB_experimentdevice" USING btree (experiment_id);


--
-- Name: battDB_filefolder_parent_id_62154397; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_filefolder_parent_id_62154397" ON public."battDB_filefolder" USING btree (parent_id);


--
-- Name: battDB_filefolder_slug_0c44081c; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_filefolder_slug_0c44081c" ON public."battDB_filefolder" USING btree (slug);


--
-- Name: battDB_filefolder_slug_0c44081c_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_filefolder_slug_0c44081c_like" ON public."battDB_filefolder" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_filefolder_tree_id_d1309d6d; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_filefolder_tree_id_d1309d6d" ON public."battDB_filefolder" USING btree (tree_id);


--
-- Name: battDB_filefolder_user_owner_id_a306e59e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_filefolder_user_owner_id_a306e59e" ON public."battDB_filefolder" USING btree (user_owner_id);


--
-- Name: battDB_harvester_attach_to_equipment_id_43c580f1; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_harvester_attach_to_equipment_id_43c580f1" ON public."battDB_harvester" USING btree (equipment_type_id);


--
-- Name: battDB_harvester_attach_to_experiment_id_785e6338; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_harvester_attach_to_experiment_id_785e6338" ON public."battDB_harvester" USING btree (attach_to_experiment_id);


--
-- Name: battDB_harvester_slug_23fa0482; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_harvester_slug_23fa0482" ON public."battDB_harvester" USING btree (slug);


--
-- Name: battDB_harvester_slug_23fa0482_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_harvester_slug_23fa0482_like" ON public."battDB_harvester" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_harvester_user_owner_id_1e9ff937; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_harvester_user_owner_id_1e9ff937" ON public."battDB_harvester" USING btree (user_owner_id);


--
-- Name: battDB_parser_slug_c95729d2; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_parser_slug_c95729d2" ON public."battDB_parser" USING btree (slug);


--
-- Name: battDB_parser_slug_c95729d2_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_parser_slug_c95729d2_like" ON public."battDB_parser" USING btree (slug varchar_pattern_ops);


--
-- Name: battDB_parser_user_owner_id_5beb846d; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_parser_user_owner_id_5beb846d" ON public."battDB_parser" USING btree (user_owner_id);


--
-- Name: battDB_signaltype_parameter_id_b769c552; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_signaltype_parameter_id_b769c552" ON public."battDB_signaltype" USING btree (parameter_id);


--
-- Name: battDB_signaltype_parser_id_71e1d0a1; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX "battDB_signaltype_parser_id_71e1d0a1" ON public."battDB_signaltype" USING btree (parser_id);


--
-- Name: common_org_name_062cae2a_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_org_name_062cae2a_like ON public.common_org USING btree (name varchar_pattern_ops);


--
-- Name: common_org_slug_9b1804cf; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_org_slug_9b1804cf ON public.common_org USING btree (slug);


--
-- Name: common_org_slug_9b1804cf_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_org_slug_9b1804cf_like ON public.common_org USING btree (slug varchar_pattern_ops);


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
-- Name: common_paper_slug_0fcf4828; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paper_slug_0fcf4828 ON public.common_paper USING btree (slug);


--
-- Name: common_paper_slug_0fcf4828_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paper_slug_0fcf4828_like ON public.common_paper USING btree (slug varchar_pattern_ops);


--
-- Name: common_paper_user_owner_id_ea0784cc; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_paper_user_owner_id_ea0784cc ON public.common_paper USING btree (user_owner_id);


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
-- Name: common_uploadedfile_hash_724f1a2d_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_uploadedfile_hash_724f1a2d_like ON public.common_uploadedfile USING btree (hash varchar_pattern_ops);


--
-- Name: common_uploadedfile_user_owner_id_fb5e27a2; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX common_uploadedfile_user_owner_id_fb5e27a2 ON public.common_uploadedfile USING btree (user_owner_id);


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
-- Name: dfndb_data_slug_2de6ba87; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_data_slug_2de6ba87 ON public.dfndb_data USING btree (slug);


--
-- Name: dfndb_data_slug_2de6ba87_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_data_slug_2de6ba87_like ON public.dfndb_data USING btree (slug varchar_pattern_ops);


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
-- Name: dfndb_material_slug_0f6947a2; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_material_slug_0f6947a2 ON public.dfndb_material USING btree (slug);


--
-- Name: dfndb_material_slug_0f6947a2_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_material_slug_0f6947a2_like ON public.dfndb_material USING btree (slug varchar_pattern_ops);


--
-- Name: dfndb_method_owner_id_a24ddb1e; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_method_owner_id_a24ddb1e ON public.dfndb_method USING btree (user_owner_id);


--
-- Name: dfndb_method_slug_0947f84f; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_method_slug_0947f84f ON public.dfndb_method USING btree (slug);


--
-- Name: dfndb_method_slug_0947f84f_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_method_slug_0947f84f_like ON public.dfndb_method USING btree (slug varchar_pattern_ops);


--
-- Name: dfndb_parameter_owner_id_870086c2; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_parameter_owner_id_870086c2 ON public.dfndb_parameter USING btree (user_owner_id);


--
-- Name: dfndb_parameter_slug_d3fcf937; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_parameter_slug_d3fcf937 ON public.dfndb_parameter USING btree (slug);


--
-- Name: dfndb_parameter_slug_d3fcf937_like; Type: INDEX; Schema: public; Owner: towen
--

CREATE INDEX dfndb_parameter_slug_d3fcf937_like ON public.dfndb_parameter USING btree (slug varchar_pattern_ops);


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
-- Name: battDB_batchdevice battDB_batchdevice_batch_id_8cefc0b1_fk_battDB_devicebatch_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_batchdevice"
    ADD CONSTRAINT "battDB_batchdevice_batch_id_8cefc0b1_fk_battDB_devicebatch_id" FOREIGN KEY (batch_id) REFERENCES public."battDB_devicebatch"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_datacolumn battDB_datacolumn_data_file_id_df73df9e_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datacolumn"
    ADD CONSTRAINT "battDB_datacolumn_data_file_id_df73df9e_fk_battDB_ex" FOREIGN KEY (data_file_id) REFERENCES public."battDB_experimentdatafile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_datacolumn battDB_datacolumn_device_id_bee39a70_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datacolumn"
    ADD CONSTRAINT "battDB_datacolumn_device_id_bee39a70_fk_battDB_ex" FOREIGN KEY (device_id) REFERENCES public."battDB_experimentdevice"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_datacolumn battDB_datacolumn_parameter_id_1d518565_fk_dfndb_parameter_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_datacolumn"
    ADD CONSTRAINT "battDB_datacolumn_parameter_id_1d518565_fk_dfndb_parameter_id" FOREIGN KEY (parameter_id) REFERENCES public.dfndb_parameter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicebatch battDB_devicebatch_manufacturer_id_85675f1a_fk_common_org_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_manufacturer_id_85675f1a_fk_common_org_id" FOREIGN KEY (manufacturer_id) REFERENCES public.common_org(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicebatch battDB_devicebatch_manufacturing_protoc_0ffaa425_fk_dfndb_met; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_manufacturing_protoc_0ffaa425_fk_dfndb_met" FOREIGN KEY (manufacturing_protocol_id) REFERENCES public.dfndb_method(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicebatch battDB_devicebatch_parent_id_e0be7099_fk_battDB_devicebatch_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_parent_id_e0be7099_fk_battDB_devicebatch_id" FOREIGN KEY (parent_id) REFERENCES public."battDB_devicebatch"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicebatch battDB_devicebatch_specification_id_528663e7_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicebatch"
    ADD CONSTRAINT "battDB_devicebatch_specification_id_528663e7_fk_battDB_de" FOREIGN KEY (specification_id) REFERENCES public."battDB_devicespecification"(id) DEFERRABLE INITIALLY DEFERRED;


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
-- Name: battDB_deviceconfignode battDB_deviceconfign_config_id_08206ff9_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfignode"
    ADD CONSTRAINT "battDB_deviceconfign_config_id_08206ff9_fk_battDB_de" FOREIGN KEY (config_id) REFERENCES public."battDB_deviceconfig"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceconfignode battDB_deviceconfign_device_id_21bed58f_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceconfignode"
    ADD CONSTRAINT "battDB_deviceconfign_device_id_21bed58f_fk_battDB_de" FOREIGN KEY (device_id) REFERENCES public."battDB_devicespecification"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceparameter battDB_deviceparamet_material_id_0e7af7bd_fk_dfndb_mat; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceparameter"
    ADD CONSTRAINT "battDB_deviceparamet_material_id_0e7af7bd_fk_dfndb_mat" FOREIGN KEY (material_id) REFERENCES public.dfndb_material(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceparameter battDB_deviceparamet_parameter_id_5107f443_fk_dfndb_par; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceparameter"
    ADD CONSTRAINT "battDB_deviceparamet_parameter_id_5107f443_fk_dfndb_par" FOREIGN KEY (parameter_id) REFERENCES public.dfndb_parameter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_deviceparameter battDB_deviceparamet_spec_id_5c622dac_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_deviceparameter"
    ADD CONSTRAINT "battDB_deviceparamet_spec_id_5c622dac_fk_battDB_de" FOREIGN KEY (spec_id) REFERENCES public."battDB_devicespecification"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicespecification battDB_devicespecifi_device_type_id_81af892f_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicespecification"
    ADD CONSTRAINT "battDB_devicespecifi_device_type_id_81af892f_fk_battDB_de" FOREIGN KEY (device_type_id) REFERENCES public."battDB_devicespecification"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicespecification battDB_devicespecifi_parent_id_5f4c7c57_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicespecification"
    ADD CONSTRAINT "battDB_devicespecifi_parent_id_5f4c7c57_fk_battDB_de" FOREIGN KEY (parent_id) REFERENCES public."battDB_devicespecification"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_devicespecification battDB_devicespecifi_user_owner_id_35f6fdb1_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_devicespecification"
    ADD CONSTRAINT "battDB_devicespecifi_user_owner_id_35f6fdb1_fk_auth_user" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipment battDB_equipment_default_parser_id_d9728b28_fk_battDB_parser_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_default_parser_id_d9728b28_fk_battDB_parser_id" FOREIGN KEY (default_parser_id) REFERENCES public."battDB_parser"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipment battDB_equipment_manufacturer_id_52eef8ee_fk_common_org_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_manufacturer_id_52eef8ee_fk_common_org_id" FOREIGN KEY (manufacturer_id) REFERENCES public.common_org(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipment battDB_equipment_specification_id_cae1bbf7_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_specification_id_cae1bbf7_fk_battDB_de" FOREIGN KEY (specification_id) REFERENCES public."battDB_devicespecification"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipment battDB_equipment_user_owner_id_bbb9f49e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_user_owner_id_bbb9f49e_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment battDB_experiment_config_id_308e8e11_fk_battDB_deviceconfig_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_config_id_308e8e11_fk_battDB_deviceconfig_id" FOREIGN KEY (config_id) REFERENCES public."battDB_deviceconfig"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment battDB_experiment_folder_id_ffc45c6a_fk_battDB_filefolder_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_folder_id_ffc45c6a_fk_battDB_filefolder_id" FOREIGN KEY (folder_id) REFERENCES public."battDB_filefolder"(id) DEFERRABLE INITIALLY DEFERRED;


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
-- Name: battDB_experimentdatafile battDB_experimentdat_raw_data_file_id_91752398_fk_common_up; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdat_raw_data_file_id_91752398_fk_common_up" FOREIGN KEY (raw_data_file_id) REFERENCES public.common_uploadedfile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdatafile battDB_experimentdat_use_parser_id_fffb2715_fk_battDB_pa; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdat_use_parser_id_fffb2715_fk_battDB_pa" FOREIGN KEY (use_parser_id) REFERENCES public."battDB_parser"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdatafile battDB_experimentdat_user_owner_id_f8f951f2_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdatafile"
    ADD CONSTRAINT "battDB_experimentdat_user_owner_id_f8f951f2_fk_auth_user" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdevice battDB_experimentdev_data_file_id_1a1175e3_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdevice"
    ADD CONSTRAINT "battDB_experimentdev_data_file_id_1a1175e3_fk_battDB_ex" FOREIGN KEY (data_file_id) REFERENCES public."battDB_experimentdatafile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdevice battDB_experimentdev_deviceBatch_id_eccc8b4a_fk_battDB_de; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdevice"
    ADD CONSTRAINT "battDB_experimentdev_deviceBatch_id_eccc8b4a_fk_battDB_de" FOREIGN KEY ("deviceBatch_id") REFERENCES public."battDB_devicebatch"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentdevice battDB_experimentdev_experiment_id_566fbea4_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_experimentdevice"
    ADD CONSTRAINT "battDB_experimentdev_experiment_id_566fbea4_fk_battDB_ex" FOREIGN KEY (experiment_id) REFERENCES public."battDB_experiment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_filefolder battDB_filefolder_parent_id_62154397_fk_battDB_filefolder_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_filefolder"
    ADD CONSTRAINT "battDB_filefolder_parent_id_62154397_fk_battDB_filefolder_id" FOREIGN KEY (parent_id) REFERENCES public."battDB_filefolder"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_filefolder battDB_filefolder_user_owner_id_a306e59e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_filefolder"
    ADD CONSTRAINT "battDB_filefolder_user_owner_id_a306e59e_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_harvester battDB_harvester_attach_to_experiment_785e6338_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_harvester"
    ADD CONSTRAINT "battDB_harvester_attach_to_experiment_785e6338_fk_battDB_ex" FOREIGN KEY (attach_to_experiment_id) REFERENCES public."battDB_experiment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_harvester battDB_harvester_equipment_type_id_04125ef9_fk_battDB_eq; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_harvester"
    ADD CONSTRAINT "battDB_harvester_equipment_type_id_04125ef9_fk_battDB_eq" FOREIGN KEY (equipment_type_id) REFERENCES public."battDB_equipment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_harvester battDB_harvester_user_owner_id_1e9ff937_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_harvester"
    ADD CONSTRAINT "battDB_harvester_user_owner_id_1e9ff937_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_parser battDB_parser_user_owner_id_5beb846d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_parser"
    ADD CONSTRAINT "battDB_parser_user_owner_id_5beb846d_fk_auth_user_id" FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_signaltype battDB_signaltype_parameter_id_b769c552_fk_dfndb_parameter_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_signaltype"
    ADD CONSTRAINT "battDB_signaltype_parameter_id_b769c552_fk_dfndb_parameter_id" FOREIGN KEY (parameter_id) REFERENCES public.dfndb_parameter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_signaltype battDB_signaltype_parser_id_71e1d0a1_fk_battDB_parser_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public."battDB_signaltype"
    ADD CONSTRAINT "battDB_signaltype_parser_id_71e1d0a1_fk_battDB_parser_id" FOREIGN KEY (parser_id) REFERENCES public."battDB_parser"(id) DEFERRABLE INITIALLY DEFERRED;


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
-- Name: common_uploadedfile common_uploadedfile_user_owner_id_fb5e27a2_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: towen
--

ALTER TABLE ONLY public.common_uploadedfile
    ADD CONSTRAINT common_uploadedfile_user_owner_id_fb5e27a2_fk_auth_user_id FOREIGN KEY (user_owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


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

