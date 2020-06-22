-- Table: public.usuario

-- DROP TABLE public.usuario;

CREATE TABLE public.usuario
(
  id serial NOT NULL,
  nome character varying(255) NOT NULL,
  idade character varying(255) NOT NULL,
  profissao character varying(255) NOT NULL,
  CONSTRAINT usuario_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.usuario
  OWNER TO ponto_tel_user;




-- Table: public.empresa

-- DROP TABLE public.empresa;

CREATE TABLE public.empresa
(
  id serial NOT NULL,
  symbol character varying(255) NOT NULL,
  name character varying(255) NOT NULL,
  type character varying(255) NOT NULL,
  region character varying(255) NOT NULL,
  "marketOpen" character varying(255) NOT NULL,
  "marketClose" character varying(255) NOT NULL,
  timezone character varying(255) NOT NULL,
  currency character varying(255) NOT NULL,
  "matchScore" character varying(255) NOT NULL,
  CONSTRAINT empresa_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.empresa
  OWNER TO ponto_tel_user;












-- Table: public.cotacao

-- DROP TABLE public.cotacao;

CREATE TABLE public.cotacao
(
  id serial NOT NULL,
  open character varying(255) NOT NULL,
  high character varying(255) NOT NULL,
  low character varying(255) NOT NULL,
  close character varying(255) NOT NULL,
  volume character varying(255) NOT NULL,
  empresa_id integer,
  date character varying(255),
  CONSTRAINT cotacao_pkey PRIMARY KEY (id),
  CONSTRAINT cotacao_empresa_id_fkey FOREIGN KEY (empresa_id)
      REFERENCES public.empresa (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.cotacao
  OWNER TO ponto_tel_user;



