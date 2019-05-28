--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.17
-- Dumped by pg_dump version 9.5.17

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: english; Type: TABLE; Schema: public; Owner: justin
--

CREATE TABLE public.english (
    id integer NOT NULL,
    word character varying
);


ALTER TABLE public.english OWNER TO justin;

--
-- Name: english_id_seq; Type: SEQUENCE; Schema: public; Owner: justin
--

CREATE SEQUENCE public.english_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.english_id_seq OWNER TO justin;

--
-- Name: english_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: justin
--

ALTER SEQUENCE public.english_id_seq OWNED BY public.english.id;


--
-- Name: pairengesp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pairengesp (
    id integer NOT NULL,
    engid integer,
    espid integer,
    timescorrect integer DEFAULT 0,
    timesincorrect integer DEFAULT 0
);


ALTER TABLE public.pairengesp OWNER TO postgres;

--
-- Name: pairengesp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pairengesp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pairengesp_id_seq OWNER TO postgres;

--
-- Name: pairengesp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pairengesp_id_seq OWNED BY public.pairengesp.id;


--
-- Name: spanish; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spanish (
    id integer NOT NULL,
    word character varying
);


ALTER TABLE public.spanish OWNER TO postgres;

--
-- Name: spanish_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spanish_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.spanish_id_seq OWNER TO postgres;

--
-- Name: spanish_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spanish_id_seq OWNED BY public.spanish.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: justin
--

ALTER TABLE ONLY public.english ALTER COLUMN id SET DEFAULT nextval('public.english_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pairengesp ALTER COLUMN id SET DEFAULT nextval('public.pairengesp_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spanish ALTER COLUMN id SET DEFAULT nextval('public.spanish_id_seq'::regclass);


--
-- Data for Name: english; Type: TABLE DATA; Schema: public; Owner: justin
--

COPY public.english (id, word) FROM stdin;
1	to try
2	request
3	sense
4	arrives
5	to carry
6	jumps
7	climb
8	true
9	mirror
10	screen
21	Both
22	Act
23	besides (Anyway)
24	Looking for
25	In charge / position
26	True
27	place
28	Commitment
29	Course
30	Developing
31	Efforts
32	Success
33	Explain
34	failure
35	were going
36	Couples
37	Asked
38	try out
39	Steep / Deep
40	Proposal
41	test
42	Put
43	positions / places
44	Simple / Plain / Straightforward
45	Perhaps
46	Start
47	(to) Arrive
48	Arrives
49	Arrived
50	Carry
51	Carried
52	Worn
53	Resourcess
54	(they) meet
55	Jumps
56	Felt
57	Shadow
58	Climbs
59	had
60	Taken
61	Lived
62	(he/she) Come
63	(I) seen
64	Cooked
65	Spoken
66	Left
\.


--
-- Name: english_id_seq; Type: SEQUENCE SET; Schema: public; Owner: justin
--

SELECT pg_catalog.setval('public.english_id_seq', 66, true);


--
-- Data for Name: pairengesp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pairengesp (id, engid, espid, timescorrect, timesincorrect) FROM stdin;
38	45	35	3	0
30	37	27	3	0
36	43	33	3	1
34	41	31	3	1
33	40	30	3	0
35	42	32	3	0
61	66	57	4	1
22	29	19	3	1
20	27	17	3	2
21	28	18	3	3
17	24	14	4	0
15	22	12	4	0
16	23	13	4	0
14	21	11	4	0
19	26	16	4	0
50	57	47	4	0
18	25	15	4	0
49	56	46	4	2
54	61	51	4	0
52	59	49	4	1
53	60	50	4	2
51	58	48	4	0
58	64	55	4	0
55	62	52	4	2
57	63	54	4	1
59	65	56	4	0
41	48	38	4	4
42	49	39	4	3
40	47	37	4	3
39	46	36	4	0
46	53	43	4	0
45	52	42	4	8
44	51	41	4	8
43	50	40	4	2
47	54	44	4	0
6	6	9	7	3
48	55	45	4	0
7	7	10	7	2
10	10	3	7	1
9	9	2	7	0
3	3	5	7	0
5	5	7	7	0
2	2	4	8	0
1	1	1	8	0
4	4	6	7	0
8	8	8	8	0
25	32	22	3	0
24	31	21	3	1
23	30	20	3	1
26	33	23	3	0
29	36	26	3	0
32	39	29	3	0
27	34	24	3	0
28	35	25	3	0
37	44	34	3	2
31	38	28	3	1
\.


--
-- Name: pairengesp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pairengesp_id_seq', 64, true);


--
-- Data for Name: spanish; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spanish (id, word) FROM stdin;
1	tratar
2	espejo
3	pantalla
4	pedido
5	sentido
6	llega
7	lleva
8	cierto
9	salta
10	sube
11	Ambos
12	Actuar
13	Addemás
14	Buscas
15	Cargo
16	Cierto
17	Colocar
18	Compromiso
19	Curso
20	Desarrollado
21	Esfuerzos
22	Éxito
23	Explicar
24	Fracasco
25	Iban
26	Parejas
27	Pedido
28	Probar
29	Profundo
30	Propuesta
31	Prueba
32	Puesto
33	Puestos
34	Secilla
35	Quizás
36	Iniciar
37	Llegar
38	Llega
39	llegado
40	llevar
41	llevó
42	llevado
43	Recursos
44	Reúnen
45	Salta
46	Sentido
47	Sombra
48	Sube
49	Tenido
50	Tomado
51	Vivido
52	Venido
53	Verdadera
54	Visto
55	Cocinado
56	Hablado
57	Dejado
\.


--
-- Name: spanish_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.spanish_id_seq', 57, true);


--
-- Name: english_pkey; Type: CONSTRAINT; Schema: public; Owner: justin
--

ALTER TABLE ONLY public.english
    ADD CONSTRAINT english_pkey PRIMARY KEY (id);


--
-- Name: pairengesp_engid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pairengesp
    ADD CONSTRAINT pairengesp_engid_key UNIQUE (engid);


--
-- Name: pairengesp_espid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pairengesp
    ADD CONSTRAINT pairengesp_espid_key UNIQUE (espid);


--
-- Name: pairengesp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pairengesp
    ADD CONSTRAINT pairengesp_pkey PRIMARY KEY (id);


--
-- Name: spanish_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spanish
    ADD CONSTRAINT spanish_pkey PRIMARY KEY (id);


--
-- Name: pairengesp_engid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pairengesp
    ADD CONSTRAINT pairengesp_engid_fkey FOREIGN KEY (engid) REFERENCES public.english(id);


--
-- Name: pairengesp_espid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pairengesp
    ADD CONSTRAINT pairengesp_espid_fkey FOREIGN KEY (espid) REFERENCES public.spanish(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: TABLE english; Type: ACL; Schema: public; Owner: justin
--

REVOKE ALL ON TABLE public.english FROM PUBLIC;
REVOKE ALL ON TABLE public.english FROM justin;
GRANT ALL ON TABLE public.english TO justin;


--
-- Name: SEQUENCE english_id_seq; Type: ACL; Schema: public; Owner: justin
--

REVOKE ALL ON SEQUENCE public.english_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.english_id_seq FROM justin;
GRANT ALL ON SEQUENCE public.english_id_seq TO justin;


--
-- Name: TABLE pairengesp; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.pairengesp FROM PUBLIC;
REVOKE ALL ON TABLE public.pairengesp FROM postgres;
GRANT ALL ON TABLE public.pairengesp TO postgres;
GRANT ALL ON TABLE public.pairengesp TO justin;


--
-- Name: SEQUENCE pairengesp_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.pairengesp_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.pairengesp_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.pairengesp_id_seq TO postgres;
GRANT SELECT,USAGE ON SEQUENCE public.pairengesp_id_seq TO justin;


--
-- Name: TABLE spanish; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.spanish FROM PUBLIC;
REVOKE ALL ON TABLE public.spanish FROM postgres;
GRANT ALL ON TABLE public.spanish TO postgres;
GRANT ALL ON TABLE public.spanish TO justin;


--
-- Name: SEQUENCE spanish_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.spanish_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.spanish_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.spanish_id_seq TO postgres;
GRANT SELECT,USAGE ON SEQUENCE public.spanish_id_seq TO justin;


--
-- PostgreSQL database dump complete
--

