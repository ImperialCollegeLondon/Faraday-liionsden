--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3 (Debian 12.3-1+b1)
-- Dumped by pg_dump version 12.3 (Debian 12.3-1+b1)

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
-- Name: auth_group; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO tom;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO tom;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO tom;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO tom;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO tom;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO tom;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO tom;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO tom;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO tom;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO tom;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO tom;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO tom;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: battDB_cell; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_cell" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL,
    batch_id integer,
    separator_id integer
);


ALTER TABLE public."battDB_cell" OWNER TO tom;

--
-- Name: battDB_cell_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_cell_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_cell_id_seq" OWNER TO tom;

--
-- Name: battDB_cell_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_cell_id_seq" OWNED BY public."battDB_cell".id;


--
-- Name: battDB_cellbatch; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_cellbatch" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL,
    manufactured_on date,
    cells_schema jsonb NOT NULL,
    manufacturer_id integer
);


ALTER TABLE public."battDB_cellbatch" OWNER TO tom;

--
-- Name: battDB_cellbatch_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_cellbatch_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_cellbatch_id_seq" OWNER TO tom;

--
-- Name: battDB_cellbatch_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_cellbatch_id_seq" OWNED BY public."battDB_cellbatch".id;


--
-- Name: battDB_cellconfig; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_cellconfig" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL
);


ALTER TABLE public."battDB_cellconfig" OWNER TO tom;

--
-- Name: battDB_cellconfig_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_cellconfig_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_cellconfig_id_seq" OWNER TO tom;

--
-- Name: battDB_cellconfig_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_cellconfig_id_seq" OWNED BY public."battDB_cellconfig".id;


--
-- Name: battDB_cellseparator; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_cellseparator" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL
);


ALTER TABLE public."battDB_cellseparator" OWNER TO tom;

--
-- Name: battDB_cellseparator_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_cellseparator_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_cellseparator_id_seq" OWNER TO tom;

--
-- Name: battDB_cellseparator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_cellseparator_id_seq" OWNED BY public."battDB_cellseparator".id;


--
-- Name: battDB_equipment; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_equipment" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL,
    "serialNo" character varying(64) NOT NULL,
    type_id integer
);


ALTER TABLE public."battDB_equipment" OWNER TO tom;

--
-- Name: battDB_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_equipment_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_equipment_id_seq" OWNER TO tom;

--
-- Name: battDB_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_equipment_id_seq" OWNED BY public."battDB_equipment".id;


--
-- Name: battDB_equipmenttype; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_equipmenttype" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL,
    manufacturer_id integer
);


ALTER TABLE public."battDB_equipmenttype" OWNER TO tom;

--
-- Name: battDB_equipmenttype_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_equipmenttype_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_equipmenttype_id_seq" OWNER TO tom;

--
-- Name: battDB_equipmenttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_equipmenttype_id_seq" OWNED BY public."battDB_equipmenttype".id;


--
-- Name: battDB_experiment; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_experiment" (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    date date NOT NULL,
    raw_data_file character varying(100),
    parameters jsonb NOT NULL,
    analysis jsonb NOT NULL,
    apparatus_id integer,
    owner_id integer,
    processed_data_file character varying(100)
);


ALTER TABLE public."battDB_experiment" OWNER TO tom;

--
-- Name: battDB_experiment_cells; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_experiment_cells" (
    id integer NOT NULL,
    experiment_id integer NOT NULL,
    cell_id integer NOT NULL
);


ALTER TABLE public."battDB_experiment_cells" OWNER TO tom;

--
-- Name: battDB_experiment_cells_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_experiment_cells_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_experiment_cells_id_seq" OWNER TO tom;

--
-- Name: battDB_experiment_cells_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_experiment_cells_id_seq" OWNED BY public."battDB_experiment_cells".id;


--
-- Name: battDB_experiment_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_experiment_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_experiment_id_seq" OWNER TO tom;

--
-- Name: battDB_experiment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_experiment_id_seq" OWNED BY public."battDB_experiment".id;


--
-- Name: battDB_experimentalapparatus; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_experimentalapparatus" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL,
    protocol_id integer,
    photo character varying(100),
    "cellConfig_id" integer
);


ALTER TABLE public."battDB_experimentalapparatus" OWNER TO tom;

--
-- Name: battDB_experimentalapparatus_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_experimentalapparatus_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_experimentalapparatus_id_seq" OWNER TO tom;

--
-- Name: battDB_experimentalapparatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_experimentalapparatus_id_seq" OWNED BY public."battDB_experimentalapparatus".id;


--
-- Name: battDB_experimentalapparatus_testEquipment; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_experimentalapparatus_testEquipment" (
    id integer NOT NULL,
    experimentalapparatus_id integer NOT NULL,
    equipment_id integer NOT NULL
);


ALTER TABLE public."battDB_experimentalapparatus_testEquipment" OWNER TO tom;

--
-- Name: battDB_experimentalapparatus_testEquipment_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_experimentalapparatus_testEquipment_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_experimentalapparatus_testEquipment_id_seq" OWNER TO tom;

--
-- Name: battDB_experimentalapparatus_testEquipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_experimentalapparatus_testEquipment_id_seq" OWNED BY public."battDB_experimentalapparatus_testEquipment".id;


--
-- Name: battDB_manufacturer; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_manufacturer" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL
);


ALTER TABLE public."battDB_manufacturer" OWNER TO tom;

--
-- Name: battDB_manufacturer_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_manufacturer_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_manufacturer_id_seq" OWNER TO tom;

--
-- Name: battDB_manufacturer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_manufacturer_id_seq" OWNED BY public."battDB_manufacturer".id;


--
-- Name: battDB_signaltype; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_signaltype" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL
);


ALTER TABLE public."battDB_signaltype" OWNER TO tom;

--
-- Name: battDB_signaltype_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_signaltype_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_signaltype_id_seq" OWNER TO tom;

--
-- Name: battDB_signaltype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_signaltype_id_seq" OWNED BY public."battDB_signaltype".id;


--
-- Name: battDB_testprotocol; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public."battDB_testprotocol" (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    attributes jsonb NOT NULL,
    description text NOT NULL,
    parameters jsonb NOT NULL
);


ALTER TABLE public."battDB_testprotocol" OWNER TO tom;

--
-- Name: battDB_testprotocol_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public."battDB_testprotocol_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."battDB_testprotocol_id_seq" OWNER TO tom;

--
-- Name: battDB_testprotocol_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public."battDB_testprotocol_id_seq" OWNED BY public."battDB_testprotocol".id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: tom
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


ALTER TABLE public.django_admin_log OWNER TO tom;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO tom;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO tom;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO tom;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO tom;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: tom
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO tom;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tom
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: tom
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO tom;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: battDB_cell id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cell" ALTER COLUMN id SET DEFAULT nextval('public."battDB_cell_id_seq"'::regclass);


--
-- Name: battDB_cellbatch id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellbatch" ALTER COLUMN id SET DEFAULT nextval('public."battDB_cellbatch_id_seq"'::regclass);


--
-- Name: battDB_cellconfig id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellconfig" ALTER COLUMN id SET DEFAULT nextval('public."battDB_cellconfig_id_seq"'::regclass);


--
-- Name: battDB_cellseparator id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellseparator" ALTER COLUMN id SET DEFAULT nextval('public."battDB_cellseparator_id_seq"'::regclass);


--
-- Name: battDB_equipment id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipment" ALTER COLUMN id SET DEFAULT nextval('public."battDB_equipment_id_seq"'::regclass);


--
-- Name: battDB_equipmenttype id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipmenttype" ALTER COLUMN id SET DEFAULT nextval('public."battDB_equipmenttype_id_seq"'::regclass);


--
-- Name: battDB_experiment id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experiment_id_seq"'::regclass);


--
-- Name: battDB_experiment_cells id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment_cells" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experiment_cells_id_seq"'::regclass);


--
-- Name: battDB_experimentalapparatus id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experimentalapparatus_id_seq"'::regclass);


--
-- Name: battDB_experimentalapparatus_testEquipment id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus_testEquipment" ALTER COLUMN id SET DEFAULT nextval('public."battDB_experimentalapparatus_testEquipment_id_seq"'::regclass);


--
-- Name: battDB_manufacturer id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_manufacturer" ALTER COLUMN id SET DEFAULT nextval('public."battDB_manufacturer_id_seq"'::regclass);


--
-- Name: battDB_signaltype id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_signaltype" ALTER COLUMN id SET DEFAULT nextval('public."battDB_signaltype_id_seq"'::regclass);


--
-- Name: battDB_testprotocol id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_testprotocol" ALTER COLUMN id SET DEFAULT nextval('public."battDB_testprotocol_id_seq"'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public.auth_group (id, name) FROM stdin;
1	Administrators
2	Experimenters
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: tom
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
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: tom
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
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$150000$2J7Bci8oeR8W$7IUeiZavNLMqx+xLNra875eCuEbiuXxpbFniRJl3kj0=	2020-08-11 10:09:23.615492+00	t	tom				t	t	2020-08-04 18:08:06.79837+00
2	pbkdf2_sha256$150000$xjdfdhTwRhJ2$UXRtByrTwyL9b+c/+/4ttwBrsYYx4Z3gXbi7n7MqAyo=	\N	t	jacql	Jacqueline	Edge	j.edge@imperial.ac.uk	t	t	2020-08-11 10:11:31+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: tom
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
\.


--
-- Data for Name: battDB_cell; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_cell" (id, name, attributes, batch_id, separator_id) FROM stdin;
1	MyLiPo	{}	1	\N
\.


--
-- Data for Name: battDB_cellbatch; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_cellbatch" (id, name, attributes, manufactured_on, cells_schema, manufacturer_id) FROM stdin;
1	foo	{}	2020-08-04	{}	1
\.


--
-- Data for Name: battDB_cellconfig; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_cellconfig" (id, name, attributes) FROM stdin;
1	4s	{}
\.


--
-- Data for Name: battDB_cellseparator; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_cellseparator" (id, name, attributes) FROM stdin;
1	MyMembrane	{"material": null, "porosity_pct": null}
\.


--
-- Data for Name: battDB_equipment; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_equipment" (id, name, attributes, "serialNo", type_id) FROM stdin;
1	Tom's GalvoTron 3000	{}	1234	2
\.


--
-- Data for Name: battDB_equipmenttype; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_equipmenttype" (id, name, attributes, manufacturer_id) FROM stdin;
2	GalvoTron 3000	{"channels": 10}	1
\.


--
-- Data for Name: battDB_experiment; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_experiment" (id, name, date, raw_data_file, parameters, analysis, apparatus_id, owner_id, processed_data_file) FROM stdin;
8	experiment	2020-08-05	raw_data_files/BioLogic_full_dLqsqJK.txt	{"EndVoltage": null, "StartVoltage": null}	{"MeasuredCapacity": null, "MeasuredResistance": null}	1	1	
9	foo	2020-08-05	raw_data_files/BioLogic_full_35X61jw.txt	{"EndVoltage": null, "StartVoltage": null}	{"x": {"has_data": true, "is_numeric": true}, "Ns": {"has_data": true, "is_numeric": true}, "P/W": {"has_data": true, "is_numeric": true}, "I/mA": {"has_data": true, "is_numeric": true}, "Rec#": {"has_data": true, "is_numeric": true}, "Time": {"has_data": true, "is_numeric": true}, "mode": {"has_data": true, "is_numeric": true}, "R/Ohm": {"has_data": true, "is_numeric": true}, "error": {"has_data": true, "is_numeric": true}, "ox/red": {"has_data": true, "is_numeric": true}, "Ecell/V": {"has_data": true, "is_numeric": true}, "I Range": {"has_data": true, "is_numeric": true}, "dq/mA_h": {"has_data": true, "is_numeric": true}, "num_rows": 149, "warnings": [], "control/V": {"has_data": true, "is_numeric": true}, "processed": "YES", "Energy/W_h": {"has_data": true, "is_numeric": true}, "Ns changes": {"has_data": true, "is_numeric": true}, "control/mA": {"has_data": true, "is_numeric": true}, "data_start": 101, "(Q-Qo)/mA_h": {"has_data": true, "is_numeric": true}, "counter inc": {"has_data": true, "is_numeric": true}, "Analog OUT/V": {"has_data": true, "is_numeric": true}, "Dataset_Name": "BioLogic_full_35X61jw", "Efficiency/%": {"has_data": true, "is_numeric": true}, "control/V/mA": {"has_data": true, "is_numeric": true}, "cycle number": {"has_data": true, "is_numeric": true}, "dataset_size": 101861, "Analog IN 1/V": {"has_data": true, "is_numeric": true}, "Capacity/mA_h": {"has_data": true, "is_numeric": true}, "Q charge/mA_h": {"has_data": true, "is_numeric": true}, "misc_file_data": ["BT-Lab ASCII FILE\\n", "Nb header lines : 102                         \\n", "\\n", "Modulo Bat\\n", "\\n", "Run on channel : E1 (SN 0355)\\n", "User : \\n", "Ecell ctrl range : min = 0.00 V, max = 9.00 V\\n", "Safety Limits :\\n", "\\tEcell min = 2.50 V\\n", "\\tEcell max = 4.35 V\\n", "\\tfor t > 10 ms\\n", "Acquisition started on : 08/19/2019 16:31:18\\n", "Saved on :\\n", "\\tFile : Cathode_CE1.mpr\\n", "\\tDirectory : D:\\\\Data\\\\Ryan\\\\Entropy CoinCells 18Aug\\\\\\n", "\\tHost : 192.109.209.129\\n", "Device : BCS-815 (SN 0455)\\n", "Address : 192.109.209.128\\n", "BT-Lab for windows v1.65 (software)\\n", "Internet server v1.65 (firmware)\\n", "Command interpretor v1.65 (firmware)\\n", "Electrode material : \\n", "Initial state : \\n", "Electrolyte : \\n", "Comments : \\n", "Mass of active material : 0.001 mg\\n", " at x = 0.000\\n", "Molecular weight of active material (at x = 0) : 0.001 g/mol\\n", "Atomic weight of intercalated ion : 0.001 g/mol\\n", "Acquisition started at : xo = 0.000\\n", "Number of e- transfered per intercalated ion : 1\\n", "for DX = 1, DQ = 26.802 mA.h\\n", "Battery capacity : 2.230 mA.h\\n", "Electrode surface area : 0.001 cm²\\n", "Characteristic mass : 0.001 g\\n", "Record Analogic IN 1\\n", "Cycle Definition : Charge/Discharge alternance\\n", "External device configuration :\\n", "   device type : Other\\n", "   device name : Other\\n", "   Analog OUT : \\n", "      mode : E/V\\n", "      unit : E/V\\n", "      max : 5.000 at 5.000 V\\n", "      min : 0.000 at 0.000 V\\n", "      current : 0.000\\n", "   Analog IN 1 : \\n", "      unit : E/V\\n", "      max : 5.000 at 5.000 V\\n", "      min : 0.000 at 0.000 V\\n", "Ns                  0                   1                   2                   3                   4                   5                   6                   7                   8                   9                   10                  11                  12                  13                  14                  15                  16                  17                  18                  19                  20                  21                  22                  23                  24                  25                  26                  27                  28                  29                  \\n", "ctrl_type           Rest                Rest                CC                  CV                  Rest                TO                  Rest                Rest                Rest                Rest                Rest                Rest                CC                  Rest                TO                  Rest                Rest                Rest                Rest                Rest                Rest                Loop                CV                  TO                  Rest                Rest                Rest                Rest                Rest                Rest                \\n", "Apply I/C           I                   I                   C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               C / N               \\n", "ctrl1_val                                                   0.000               4.300                                   2.700                                                                                                                                       100.000                                 100.000                                                                                                                                     100.000             2.700               4.300                                                                                                                                       \\n", "ctrl1_val_unit                                              mA                  V                                                                                                                                                                                   mA                                                                                                                                                                                                      V                                                                                                                                                               \\n", "ctrl1_val_vs                                                <None>              Ref                                                                                                                                                                                 <None>                                                                                                                                                                                                  Ref                                                                                                                                                             \\n", "ctrl2_val                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   \\n", "ctrl2_val_unit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              \\n", "ctrl2_val_vs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                \\n", "ctrl3_val                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   \\n", "ctrl3_val_unit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              \\n", "ctrl3_val_vs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                \\n", "N                   1.00                1.00                1.00                3.00                3.00                3.00                3.00                3.00                3.00                3.00                3.00                3.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                5.00                \\n", "charge/discharge    Charge              Charge              Charge              Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Discharge           Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              Charge              \\n", "ctrl_seq            0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   12                  12                  12                  0                   0                   0                   0                   0                   0                   \\n", "ctrl_repeat         0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   60                  60                  60                  0                   0                   0                   0                   0                   0                   \\n", "ctrl_trigger        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Rising Edge         Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Rising Edge         Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Rising Edge         Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        Falling Edge        \\n", "ctrl_TO_t           0.000               0.000               0.000               0.000               0.000               2.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               2.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               2.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "ctrl_TO_t_unit      d                   d                   d                   d                   d                   s                   d                   d                   d                   d                   d                   d                   d                   d                   s                   d                   d                   d                   d                   d                   d                   d                   d                   s                   d                   d                   d                   d                   d                   d                   \\n", "ctrl_Nd             6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   6                   \\n", "ctrl_Na             1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   \\n", "ctrl_corr           1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   1                   \\n", "lim_nb              1                   1                   1                   1                   1                   0                   1                   1                   1                   1                   1                   1                   2                   1                   0                   1                   1                   1                   1                   1                   1                   0                   1                   0                   1                   1                   1                   1                   1                   1                   \\n", "lim1_type           Time                Time                Time                Ecell               |I|                 Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                |I|                 \\n", "lim1_comp           >                   >                   >                   <                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   >                   <                   <                   >                   >                   >                   >                   >                   >                   \\n", "lim1_Q              Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             \\n", "lim1_value          3.000               3.000               4.300               23.000              90.000              90.000              3.000               3.000               3.000               3.000               3.000               10.000              6.000               90.000              90.000              3.000               3.000               3.000               3.000               3.000               10.000              10.000              23.000              23.000              3.000               3.000               3.000               3.000               3.000               10.000              \\n", "lim1_value_unit     d                   s                   s                   V                   mA                  mn                  d                   s                   d                   s                   d                   mn                  mn                  mn                  mn                  d                   s                   d                   s                   d                   mn                  mn                  s                   s                   d                   s                   d                   s                   d                   mA                  \\n", "lim1_action         Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       \\n", "lim1_seq            1                   2                   3                   4                   5                   6                   7                   8                   9                   10                  11                  12                  13                  14                  15                  16                  17                  18                  19                  20                  21                  22                  23                  24                  25                  26                  27                  28                  29                  30                  \\n", "lim2_type           Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Ecell               Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                \\n", "lim2_comp           <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   <                   \\n", "lim2_Q              Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             Q limit             \\n", "lim2_value          0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               2.700               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "lim2_value_unit     s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   V                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   \\n", "lim2_action         Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Goto sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       Next sequence       \\n", "lim2_seq            1                   2                   3                   4                   5                   6                   7                   8                   9                   10                  11                  12                  22                  14                  15                  16                  17                  18                  19                  20                  21                  22                  23                  24                  25                  26                  27                  28                  29                  30                  \\n", "rec_nb              0                   0                   1                   1                   1                   0                   1                   1                   1                   1                   1                   1                   1                   1                   0                   1                   1                   1                   1                   1                   1                   0                   1                   0                   1                   1                   1                   1                   1                   1                   \\n", "rec1_type           Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                Time                \\n", "rec1_value          1.000               1.000               1.000               1.000               10.000              10.000              1.000               1.000               1.000               1.000               1.000               1.000               1.000               10.000              10.000              1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               1.000               \\n", "rec1_value_unit     s                   s                   s                   mn                  s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   s                   \\n", "E range min (V)     0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               0.000               \\n", "E range max (V)     9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               9.000               \\n", "I Range             10 mA               10 mA               1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                1 mA                \\n", "I Range min         Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "I Range max         Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "I Range init        Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               Unset               \\n", "auto rest           0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   0                   \\n", "Bandwidth           4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   4                   \\n", "\\n"], "control changes": {"has_data": true, "is_numeric": true}, "first_sample_no": 102, "MeasuredCapacity": null, "Q discharge/mA_h": {"has_data": true, "is_numeric": true}, "Energy charge/W_h": {"has_data": true, "is_numeric": true}, "MeasuredResistance": null, "Energy discharge/W_h": {"has_data": true, "is_numeric": true}, "Capacitance charge/�F": {"has_data": true, "is_numeric": true}, "Capacitance discharge/�F": {"has_data": true, "is_numeric": true}}	1	1	
\.


--
-- Data for Name: battDB_experiment_cells; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_experiment_cells" (id, experiment_id, cell_id) FROM stdin;
3	8	1
4	9	1
\.


--
-- Data for Name: battDB_experimentalapparatus; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_experimentalapparatus" (id, name, attributes, protocol_id, photo, "cellConfig_id") FROM stdin;
1	Tom's Lab	{}	1	\N	\N
\.


--
-- Data for Name: battDB_experimentalapparatus_testEquipment; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_experimentalapparatus_testEquipment" (id, experimentalapparatus_id, equipment_id) FROM stdin;
1	1	1
\.


--
-- Data for Name: battDB_manufacturer; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_manufacturer" (id, name, attributes) FROM stdin;
1	BorkCorp	{}
2	Maccor	{}
\.


--
-- Data for Name: battDB_signaltype; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_signaltype" (id, name, attributes) FROM stdin;
\.


--
-- Data for Name: battDB_testprotocol; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public."battDB_testprotocol" (id, name, attributes, description, parameters) FROM stdin;
1	PyBaMM example protocol	{}	pybamm.Experiment(\r\n    [\r\n        "Discharge at C/10 for 10 hours or until 3.3 V",\r\n        "Rest for 1 hour",\r\n        "Charge at 1 A until 4.1 V",\r\n        "Hold at 4.1 V until 50 mA",\r\n        "Rest for 1 hour",\r\n    ]\r\n    * 3,	{}
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-08-04 18:13:10.226362+00	1	foo	1	[{"added": {}}]	9	1
2	2020-08-04 18:25:35.516012+00	1	BorkCorp	1	[{"added": {}}]	4	1
3	2020-08-04 18:26:04.905071+00	1	foo	2	[{"changed": {"fields": ["manufacturer"]}}]	9	1
4	2020-08-04 18:27:53.921631+00	1	MyMembrane	1	[{"added": {}}]	2	1
5	2020-08-04 18:28:19.927154+00	1	MyLiPo	1	[{"added": {}}]	1	1
6	2020-08-04 18:41:57.989858+00	2	Maccor	1	[{"added": {}}]	4	1
7	2020-08-04 18:42:29.857145+00	1	GalvoTron 3000	1	[{"added": {}}]	16	1
8	2020-08-04 18:45:01.780472+00	2	GalvoTron 3000	1	[{"added": {}}]	16	1
9	2020-08-04 18:47:34.828985+00	1	Tom's GalvoTron 3000	1	[{"added": {}}]	3	1
10	2020-08-04 18:51:08.397906+00	1	PyBaMM example protocol	1	[{"added": {}}]	6	1
11	2020-08-04 18:52:01.270893+00	1	Tom's Lab	1	[{"added": {}}]	7	1
12	2020-08-04 18:52:35.233623+00	1	GalvoTron 3000	3		16	1
13	2020-08-04 18:52:52.127136+00	1	Tom's GalvoTron 3000	2	[{"changed": {"fields": ["type"]}}]	3	1
14	2020-08-04 18:54:28.563138+00	1	Experiment object (1)	1	[{"added": {}}]	8	1
15	2020-08-04 19:17:17.174324+00	1	4s	1	[{"added": {}}]	17	1
16	2020-08-04 19:26:50.203876+00	1	test test	2	[{"changed": {"fields": ["cells", "processed_data_file"]}}]	8	1
17	2020-08-04 19:36:45.200934+00	1	test test	2	[{"changed": {"fields": ["raw_data_file", "processed_data_file"]}}]	8	1
18	2020-08-05 12:09:30.332537+00	1	tom/test test/2020-08-04	3		8	1
19	2020-08-05 12:09:41.169381+00	6	tom/test test/2020-08-05	3		8	1
20	2020-08-05 12:09:41.245333+00	5	None/test test/2020-08-05	3		8	1
21	2020-08-05 12:09:41.270701+00	4	None/test test/2020-08-05	3		8	1
22	2020-08-05 12:15:42.946927+00	3	tom/test2/2020-08-05	2	[{"changed": {"fields": ["owner", "cells", "processed_data_file"]}}]	8	1
23	2020-08-05 12:15:47.904397+00	3	tom/test2/2020-08-05	2	[]	8	1
24	2020-08-05 12:17:32.85704+00	3	tom/test2/2020-08-05	3		8	1
25	2020-08-05 12:31:33.566157+00	8	tom/experiment/2020-08-05	1	[{"added": {}}]	8	1
26	2020-08-05 23:08:50.931818+00	9	tom/foo/2020-08-05	2	[{"changed": {"fields": ["cells"]}}]	8	1
27	2020-08-05 23:16:01.095768+00	9	tom/foo/2020-08-05	2	[]	8	1
28	2020-08-05 23:16:07.479654+00	9	tom/foo/2020-08-05	2	[]	8	1
29	2020-08-05 23:33:13.820898+00	9	tom/foo/2020-08-05	2	[]	8	1
30	2020-08-05 23:34:15.902395+00	9	tom/foo/2020-08-05	2	[{"changed": {"fields": ["analysis"]}}]	8	1
31	2020-08-05 23:34:26.132466+00	9	tom/foo/2020-08-05	2	[{"changed": {"fields": ["analysis"]}}]	8	1
32	2020-08-11 10:11:31.211091+00	2	jacql	1	[{"added": {}}]	12	1
33	2020-08-11 10:12:39.09724+00	2	jacql	2	[{"changed": {"fields": ["first_name", "last_name", "email", "is_staff", "is_superuser", "user_permissions"]}}]	12	1
34	2020-08-11 10:13:06.916932+00	1	Administrators	1	[{"added": {}}]	11	1
35	2020-08-11 10:14:31.126915+00	2	Experimenters	1	[{"added": {}}]	11	1
36	2020-08-12 10:25:52.862796+00	9	tom/foo/2020-08-05	2	[]	8	1
37	2020-08-12 10:26:41.764104+00	9	tom/foo/2020-08-05	2	[]	8	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: tom
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
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-08-04 18:06:03.247234+00
2	auth	0001_initial	2020-08-04 18:06:03.581176+00
3	battDB	0001_initial	2020-08-04 18:06:04.868539+00
4	admin	0001_initial	2020-08-04 18:07:21.857673+00
5	admin	0002_logentry_remove_auto_add	2020-08-04 18:07:21.984528+00
6	admin	0003_logentry_add_action_flag_choices	2020-08-04 18:07:22.066678+00
7	contenttypes	0002_remove_content_type_name	2020-08-04 18:07:22.128877+00
8	auth	0002_alter_permission_name_max_length	2020-08-04 18:07:22.180271+00
9	auth	0003_alter_user_email_max_length	2020-08-04 18:07:22.241102+00
10	auth	0004_alter_user_username_opts	2020-08-04 18:07:22.298791+00
11	auth	0005_alter_user_last_login_null	2020-08-04 18:07:22.360328+00
12	auth	0006_require_contenttypes_0002	2020-08-04 18:07:22.413536+00
13	auth	0007_alter_validators_add_error_messages	2020-08-04 18:07:22.463504+00
14	auth	0008_alter_user_username_max_length	2020-08-04 18:07:22.555198+00
15	auth	0009_alter_user_last_name_max_length	2020-08-04 18:07:22.604918+00
16	auth	0010_alter_group_name_max_length	2020-08-04 18:07:22.665178+00
17	auth	0011_update_proxy_permissions	2020-08-04 18:07:22.755407+00
18	sessions	0001_initial	2020-08-04 18:07:22.913476+00
19	battDB	0002_auto_20200804_1838	2020-08-04 18:38:40.04937+00
20	battDB	0003_equipment_type	2020-08-04 18:39:59.74901+00
21	battDB	0004_equipmenttype_manufacturer	2020-08-04 18:41:29.155848+00
22	battDB	0005_auto_20200804_1856	2020-08-04 18:57:00.082477+00
23	battDB	0006_experimentalapparatus_photo	2020-08-04 19:01:27.431661+00
24	battDB	0007_auto_20200804_1915	2020-08-04 19:15:13.651658+00
25	battDB	0008_experimentalapparatus_cellconfig	2020-08-04 19:15:40.10692+00
26	battDB	0009_auto_20200804_1920	2020-08-04 19:20:38.723312+00
27	battDB	0010_experiment_processed_data_file	2020-08-04 19:21:22.617814+00
28	battDB	0011_auto_20200804_1926	2020-08-04 19:26:18.143222+00
29	battDB	0012_cell_separator	2020-08-05 10:58:54.136899+00
30	battDB	0013_auto_20200805_1146	2020-08-05 11:46:57.293892+00
31	battDB	0014_auto_20200805_1214	2020-08-05 12:15:06.796335+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: tom
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
kznm4zgwzhdw2pczzmghrq040i9bcghc	ODkzNGRjMTU3YjY1NTAxMDE2MGU5NGRmNzU3ZWQ1YjYzOGEwMGJjNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZDc3MzRjOGIwMDg0NmM4NGU3Nzg1ZGZiZjc3ZTk4ODBhMWE3OWFiIn0=	2020-08-25 10:09:00.092024+00
h2aulckzjnz6unc9858uvjsm0l9vkte3	ODkzNGRjMTU3YjY1NTAxMDE2MGU5NGRmNzU3ZWQ1YjYzOGEwMGJjNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZDc3MzRjOGIwMDg0NmM4NGU3Nzg1ZGZiZjc3ZTk4ODBhMWE3OWFiIn0=	2020-08-25 10:09:23.656754+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 112, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 68, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 68, true);


--
-- Name: battDB_cell_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_cell_id_seq"', 1, true);


--
-- Name: battDB_cellbatch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_cellbatch_id_seq"', 1, true);


--
-- Name: battDB_cellconfig_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_cellconfig_id_seq"', 1, true);


--
-- Name: battDB_cellseparator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_cellseparator_id_seq"', 1, true);


--
-- Name: battDB_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_equipment_id_seq"', 1, true);


--
-- Name: battDB_equipmenttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_equipmenttype_id_seq"', 2, true);


--
-- Name: battDB_experiment_cells_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_experiment_cells_id_seq"', 4, true);


--
-- Name: battDB_experiment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_experiment_id_seq"', 9, true);


--
-- Name: battDB_experimentalapparatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_experimentalapparatus_id_seq"', 1, true);


--
-- Name: battDB_experimentalapparatus_testEquipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_experimentalapparatus_testEquipment_id_seq"', 1, true);


--
-- Name: battDB_manufacturer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_manufacturer_id_seq"', 2, true);


--
-- Name: battDB_signaltype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_signaltype_id_seq"', 1, false);


--
-- Name: battDB_testprotocol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public."battDB_testprotocol_id_seq"', 1, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 37, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 17, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tom
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 31, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: battDB_cell battDB_cell_name_a587c854_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cell"
    ADD CONSTRAINT "battDB_cell_name_a587c854_uniq" UNIQUE (name);


--
-- Name: battDB_cell battDB_cell_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cell"
    ADD CONSTRAINT "battDB_cell_pkey" PRIMARY KEY (id);


--
-- Name: battDB_cellbatch battDB_cellbatch_name_28a7d909_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellbatch"
    ADD CONSTRAINT "battDB_cellbatch_name_28a7d909_uniq" UNIQUE (name);


--
-- Name: battDB_cellbatch battDB_cellbatch_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellbatch"
    ADD CONSTRAINT "battDB_cellbatch_pkey" PRIMARY KEY (id);


--
-- Name: battDB_cellconfig battDB_cellconfig_name_key; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellconfig"
    ADD CONSTRAINT "battDB_cellconfig_name_key" UNIQUE (name);


--
-- Name: battDB_cellconfig battDB_cellconfig_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellconfig"
    ADD CONSTRAINT "battDB_cellconfig_pkey" PRIMARY KEY (id);


--
-- Name: battDB_cellseparator battDB_cellseparator_name_492b05f7_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellseparator"
    ADD CONSTRAINT "battDB_cellseparator_name_492b05f7_uniq" UNIQUE (name);


--
-- Name: battDB_cellseparator battDB_cellseparator_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellseparator"
    ADD CONSTRAINT "battDB_cellseparator_pkey" PRIMARY KEY (id);


--
-- Name: battDB_equipment battDB_equipment_name_85e8697e_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_name_85e8697e_uniq" UNIQUE (name);


--
-- Name: battDB_equipment battDB_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_pkey" PRIMARY KEY (id);


--
-- Name: battDB_equipmenttype battDB_equipmenttype_name_f6eb8e24_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipmenttype"
    ADD CONSTRAINT "battDB_equipmenttype_name_f6eb8e24_uniq" UNIQUE (name);


--
-- Name: battDB_equipmenttype battDB_equipmenttype_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipmenttype"
    ADD CONSTRAINT "battDB_equipmenttype_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experiment_cells battDB_experiment_cells_experiment_id_cell_id_2ba3ed8e_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment_cells"
    ADD CONSTRAINT "battDB_experiment_cells_experiment_id_cell_id_2ba3ed8e_uniq" UNIQUE (experiment_id, cell_id);


--
-- Name: battDB_experiment_cells battDB_experiment_cells_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment_cells"
    ADD CONSTRAINT "battDB_experiment_cells_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experiment battDB_experiment_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experimentalapparatus_testEquipment battDB_experimentalappar_experimentalapparatus_id_0f1ef566_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus_testEquipment"
    ADD CONSTRAINT "battDB_experimentalappar_experimentalapparatus_id_0f1ef566_uniq" UNIQUE (experimentalapparatus_id, equipment_id);


--
-- Name: battDB_experimentalapparatus battDB_experimentalapparatus_name_fae4873b_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus"
    ADD CONSTRAINT "battDB_experimentalapparatus_name_fae4873b_uniq" UNIQUE (name);


--
-- Name: battDB_experimentalapparatus battDB_experimentalapparatus_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus"
    ADD CONSTRAINT "battDB_experimentalapparatus_pkey" PRIMARY KEY (id);


--
-- Name: battDB_experimentalapparatus_testEquipment battDB_experimentalapparatus_testEquipment_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus_testEquipment"
    ADD CONSTRAINT "battDB_experimentalapparatus_testEquipment_pkey" PRIMARY KEY (id);


--
-- Name: battDB_manufacturer battDB_manufacturer_name_df40b107_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_manufacturer"
    ADD CONSTRAINT "battDB_manufacturer_name_df40b107_uniq" UNIQUE (name);


--
-- Name: battDB_manufacturer battDB_manufacturer_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_manufacturer"
    ADD CONSTRAINT "battDB_manufacturer_pkey" PRIMARY KEY (id);


--
-- Name: battDB_signaltype battDB_signaltype_name_93192e56_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_signaltype"
    ADD CONSTRAINT "battDB_signaltype_name_93192e56_uniq" UNIQUE (name);


--
-- Name: battDB_signaltype battDB_signaltype_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_signaltype"
    ADD CONSTRAINT "battDB_signaltype_pkey" PRIMARY KEY (id);


--
-- Name: battDB_testprotocol battDB_testprotocol_name_62280eb8_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_testprotocol"
    ADD CONSTRAINT "battDB_testprotocol_name_62280eb8_uniq" UNIQUE (name);


--
-- Name: battDB_testprotocol battDB_testprotocol_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_testprotocol"
    ADD CONSTRAINT "battDB_testprotocol_pkey" PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: battDB_experiment unique_namestring; Type: CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT unique_namestring UNIQUE (owner_id, name, date);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: battDB_cell_batch_id_1203f48e; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_cell_batch_id_1203f48e" ON public."battDB_cell" USING btree (batch_id);


--
-- Name: battDB_cell_name_a587c854_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_cell_name_a587c854_like" ON public."battDB_cell" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_cell_separator_id_26f13a87; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_cell_separator_id_26f13a87" ON public."battDB_cell" USING btree (separator_id);


--
-- Name: battDB_cellbatch_manufacturer_id_49a0f329; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_cellbatch_manufacturer_id_49a0f329" ON public."battDB_cellbatch" USING btree (manufacturer_id);


--
-- Name: battDB_cellbatch_name_28a7d909_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_cellbatch_name_28a7d909_like" ON public."battDB_cellbatch" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_cellconfig_name_ba125201_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_cellconfig_name_ba125201_like" ON public."battDB_cellconfig" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_cellseparator_name_492b05f7_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_cellseparator_name_492b05f7_like" ON public."battDB_cellseparator" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_equipment_name_85e8697e_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_equipment_name_85e8697e_like" ON public."battDB_equipment" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_equipment_type_id_92966c47; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_equipment_type_id_92966c47" ON public."battDB_equipment" USING btree (type_id);


--
-- Name: battDB_equipmenttype_manufacturer_id_35788864; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_equipmenttype_manufacturer_id_35788864" ON public."battDB_equipmenttype" USING btree (manufacturer_id);


--
-- Name: battDB_equipmenttype_name_f6eb8e24_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_equipmenttype_name_f6eb8e24_like" ON public."battDB_equipmenttype" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_experiment_apparatus_id_5c682616; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experiment_apparatus_id_5c682616" ON public."battDB_experiment" USING btree (apparatus_id);


--
-- Name: battDB_experiment_cells_cell_id_b488e145; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experiment_cells_cell_id_b488e145" ON public."battDB_experiment_cells" USING btree (cell_id);


--
-- Name: battDB_experiment_cells_experiment_id_9842179e; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experiment_cells_experiment_id_9842179e" ON public."battDB_experiment_cells" USING btree (experiment_id);


--
-- Name: battDB_experiment_name_4a1b5666; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experiment_name_4a1b5666" ON public."battDB_experiment" USING btree (name);


--
-- Name: battDB_experiment_name_4a1b5666_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experiment_name_4a1b5666_like" ON public."battDB_experiment" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_experiment_owner_id_ebf94468; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experiment_owner_id_ebf94468" ON public."battDB_experiment" USING btree (owner_id);


--
-- Name: battDB_experimentalapparat_equipment_id_807fef97; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experimentalapparat_equipment_id_807fef97" ON public."battDB_experimentalapparatus_testEquipment" USING btree (equipment_id);


--
-- Name: battDB_experimentalapparat_experimentalapparatus_id_4d800d2c; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experimentalapparat_experimentalapparatus_id_4d800d2c" ON public."battDB_experimentalapparatus_testEquipment" USING btree (experimentalapparatus_id);


--
-- Name: battDB_experimentalapparatus_cellConfig_id_8e623889; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experimentalapparatus_cellConfig_id_8e623889" ON public."battDB_experimentalapparatus" USING btree ("cellConfig_id");


--
-- Name: battDB_experimentalapparatus_name_fae4873b_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experimentalapparatus_name_fae4873b_like" ON public."battDB_experimentalapparatus" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_experimentalapparatus_protocol_id_73c00be9; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_experimentalapparatus_protocol_id_73c00be9" ON public."battDB_experimentalapparatus" USING btree (protocol_id);


--
-- Name: battDB_manufacturer_name_df40b107_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_manufacturer_name_df40b107_like" ON public."battDB_manufacturer" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_signaltype_name_93192e56_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_signaltype_name_93192e56_like" ON public."battDB_signaltype" USING btree (name varchar_pattern_ops);


--
-- Name: battDB_testprotocol_name_62280eb8_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX "battDB_testprotocol_name_62280eb8_like" ON public."battDB_testprotocol" USING btree (name varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: tom
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_cell battDB_cell_batch_id_1203f48e_fk_battDB_cellbatch_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cell"
    ADD CONSTRAINT "battDB_cell_batch_id_1203f48e_fk_battDB_cellbatch_id" FOREIGN KEY (batch_id) REFERENCES public."battDB_cellbatch"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_cell battDB_cell_separator_id_26f13a87_fk_battDB_cellseparator_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cell"
    ADD CONSTRAINT "battDB_cell_separator_id_26f13a87_fk_battDB_cellseparator_id" FOREIGN KEY (separator_id) REFERENCES public."battDB_cellseparator"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_cellbatch battDB_cellbatch_manufacturer_id_49a0f329_fk_battDB_ma; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_cellbatch"
    ADD CONSTRAINT "battDB_cellbatch_manufacturer_id_49a0f329_fk_battDB_ma" FOREIGN KEY (manufacturer_id) REFERENCES public."battDB_manufacturer"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipment battDB_equipment_type_id_92966c47_fk_battDB_equipmenttype_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipment"
    ADD CONSTRAINT "battDB_equipment_type_id_92966c47_fk_battDB_equipmenttype_id" FOREIGN KEY (type_id) REFERENCES public."battDB_equipmenttype"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_equipmenttype battDB_equipmenttype_manufacturer_id_35788864_fk_battDB_ma; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_equipmenttype"
    ADD CONSTRAINT "battDB_equipmenttype_manufacturer_id_35788864_fk_battDB_ma" FOREIGN KEY (manufacturer_id) REFERENCES public."battDB_manufacturer"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment battDB_experiment_apparatus_id_5c682616_fk_battDB_te; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_apparatus_id_5c682616_fk_battDB_te" FOREIGN KEY (apparatus_id) REFERENCES public."battDB_testprotocol"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment_cells battDB_experiment_ce_experiment_id_9842179e_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment_cells"
    ADD CONSTRAINT "battDB_experiment_ce_experiment_id_9842179e_fk_battDB_ex" FOREIGN KEY (experiment_id) REFERENCES public."battDB_experiment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment_cells battDB_experiment_cells_cell_id_b488e145_fk_battDB_cell_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment_cells"
    ADD CONSTRAINT "battDB_experiment_cells_cell_id_b488e145_fk_battDB_cell_id" FOREIGN KEY (cell_id) REFERENCES public."battDB_cell"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experiment battDB_experiment_owner_id_ebf94468_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experiment"
    ADD CONSTRAINT "battDB_experiment_owner_id_ebf94468_fk_auth_user_id" FOREIGN KEY (owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentalapparatus battDB_experimentala_cellConfig_id_8e623889_fk_battDB_ce; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus"
    ADD CONSTRAINT "battDB_experimentala_cellConfig_id_8e623889_fk_battDB_ce" FOREIGN KEY ("cellConfig_id") REFERENCES public."battDB_cellconfig"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentalapparatus_testEquipment battDB_experimentala_equipment_id_807fef97_fk_battDB_eq; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus_testEquipment"
    ADD CONSTRAINT "battDB_experimentala_equipment_id_807fef97_fk_battDB_eq" FOREIGN KEY (equipment_id) REFERENCES public."battDB_equipment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentalapparatus_testEquipment battDB_experimentala_experimentalapparatu_4d800d2c_fk_battDB_ex; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus_testEquipment"
    ADD CONSTRAINT "battDB_experimentala_experimentalapparatu_4d800d2c_fk_battDB_ex" FOREIGN KEY (experimentalapparatus_id) REFERENCES public."battDB_experimentalapparatus"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: battDB_experimentalapparatus battDB_experimentala_protocol_id_73c00be9_fk_battDB_te; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public."battDB_experimentalapparatus"
    ADD CONSTRAINT "battDB_experimentala_protocol_id_73c00be9_fk_battDB_te" FOREIGN KEY (protocol_id) REFERENCES public."battDB_testprotocol"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: tom
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

