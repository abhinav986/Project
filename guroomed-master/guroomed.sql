--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.3
-- Dumped by pg_dump version 9.6.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
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


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO root;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO root;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO root;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO root;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO root;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO root;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_user (
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


ALTER TABLE auth_user OWNER TO root;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO root;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO root;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO root;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO root;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO root;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: courses_category; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_category (
    id integer NOT NULL,
    name character varying(30) NOT NULL
);


ALTER TABLE courses_category OWNER TO root;

--
-- Name: courses_category_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_category_id_seq OWNER TO root;

--
-- Name: courses_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_category_id_seq OWNED BY courses_category.id;


--
-- Name: courses_course; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_course (
    id integer NOT NULL,
    title character varying(150) NOT NULL,
    ratings numeric(2,1),
    rating_count integer,
    students_enrolled integer,
    what_will_i_learn text,
    requirements text,
    description text,
    preview_video_url character varying(255),
    preview_image_url character varying(255),
    price numeric(9,2),
    discount numeric(9,2),
    no_lectures integer,
    no_hours numeric(5,1),
    level character varying(20),
    created_at date NOT NULL,
    updated_at date NOT NULL,
    course_language_id_id integer NOT NULL,
    course_subcategory_id_id integer NOT NULL,
    subtitle character varying(250),
    slug character varying(50)
);


ALTER TABLE courses_course OWNER TO root;

--
-- Name: courses_course_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_course_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_course_id_seq OWNER TO root;

--
-- Name: courses_course_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_course_id_seq OWNED BY courses_course.id;


--
-- Name: courses_course_instructor_id; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE courses_course_instructor_id (
    id integer NOT NULL,
    course_id integer NOT NULL,
    instructor_id integer NOT NULL
);


ALTER TABLE courses_course_instructor_id OWNER TO postgres;

--
-- Name: courses_course_instructor_id_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE courses_course_instructor_id_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_course_instructor_id_id_seq OWNER TO postgres;

--
-- Name: courses_course_instructor_id_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE courses_course_instructor_id_id_seq OWNED BY courses_course_instructor_id.id;


--
-- Name: courses_course_tags; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_course_tags (
    id integer NOT NULL,
    course_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE courses_course_tags OWNER TO root;

--
-- Name: courses_course_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_course_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_course_tags_id_seq OWNER TO root;

--
-- Name: courses_course_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_course_tags_id_seq OWNED BY courses_course_tags.id;


--
-- Name: courses_curriculumlecture; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_curriculumlecture (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(1500) NOT NULL,
    preview_url character varying(255),
    video_url character varying(255) NOT NULL,
    order_num integer NOT NULL,
    curriculum_section_id_id integer NOT NULL,
    lecture_type character varying(20) NOT NULL
);


ALTER TABLE courses_curriculumlecture OWNER TO root;

--
-- Name: courses_curriculumlecture_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_curriculumlecture_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_curriculumlecture_id_seq OWNER TO root;

--
-- Name: courses_curriculumlecture_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_curriculumlecture_id_seq OWNED BY courses_curriculumlecture.id;


--
-- Name: courses_curriculumsection; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_curriculumsection (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    order_num integer NOT NULL,
    course_id_id integer NOT NULL,
    duration interval NOT NULL,
    no_lectures integer NOT NULL
);


ALTER TABLE courses_curriculumsection OWNER TO root;

--
-- Name: courses_curriculumsection_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_curriculumsection_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_curriculumsection_id_seq OWNER TO root;

--
-- Name: courses_curriculumsection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_curriculumsection_id_seq OWNED BY courses_curriculumsection.id;


--
-- Name: courses_include; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_include (
    id integer NOT NULL,
    hours_on_demand integer NOT NULL,
    supplemental_resources integer NOT NULL,
    lifetime_access boolean NOT NULL,
    access_on_mobile boolean NOT NULL,
    certificate boolean NOT NULL,
    course_id_id integer NOT NULL
);


ALTER TABLE courses_include OWNER TO root;

--
-- Name: courses_include_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_include_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_include_id_seq OWNER TO root;

--
-- Name: courses_include_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_include_id_seq OWNED BY courses_include.id;


--
-- Name: courses_instructor; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_instructor (
    id integer NOT NULL,
    rating numeric(2,1) NOT NULL,
    students integer NOT NULL,
    reviews integer NOT NULL,
    courses integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE courses_instructor OWNER TO root;

--
-- Name: courses_instructor_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_instructor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_instructor_id_seq OWNER TO root;

--
-- Name: courses_instructor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_instructor_id_seq OWNED BY courses_instructor.id;


--
-- Name: courses_language; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_language (
    id integer NOT NULL,
    name character varying(20) NOT NULL
);


ALTER TABLE courses_language OWNER TO root;

--
-- Name: courses_language_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_language_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_language_id_seq OWNER TO root;

--
-- Name: courses_language_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_language_id_seq OWNED BY courses_language.id;


--
-- Name: courses_studentreview; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_studentreview (
    id integer NOT NULL,
    no_of_stars integer NOT NULL,
    about_the_course character varying(500) NOT NULL,
    about_the_instructor character varying(500) NOT NULL,
    how_course_can_improved character varying(500) NOT NULL,
    review text NOT NULL,
    course_id_id integer,
    user_id_id integer NOT NULL
);


ALTER TABLE courses_studentreview OWNER TO root;

--
-- Name: courses_studentreview_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_studentreview_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_studentreview_id_seq OWNER TO root;

--
-- Name: courses_studentreview_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_studentreview_id_seq OWNED BY courses_studentreview.id;


--
-- Name: courses_studentreviewvote; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE courses_studentreviewvote (
    id integer NOT NULL,
    "like" boolean NOT NULL,
    review_id_id integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE courses_studentreviewvote OWNER TO postgres;

--
-- Name: courses_studentreviewvote_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE courses_studentreviewvote_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_studentreviewvote_id_seq OWNER TO postgres;

--
-- Name: courses_studentreviewvote_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE courses_studentreviewvote_id_seq OWNED BY courses_studentreviewvote.id;


--
-- Name: courses_subcategory; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_subcategory (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    course_category_id_id integer NOT NULL
);


ALTER TABLE courses_subcategory OWNER TO root;

--
-- Name: courses_subcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_subcategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_subcategory_id_seq OWNER TO root;

--
-- Name: courses_subcategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_subcategory_id_seq OWNED BY courses_subcategory.id;


--
-- Name: courses_tag; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE courses_tag (
    id integer NOT NULL,
    name character varying(30) NOT NULL
);


ALTER TABLE courses_tag OWNER TO root;

--
-- Name: courses_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE courses_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courses_tag_id_seq OWNER TO root;

--
-- Name: courses_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE courses_tag_id_seq OWNED BY courses_tag.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_admin_log (
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


ALTER TABLE django_admin_log OWNER TO root;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO root;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO root;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO root;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO root;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO root;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO root;

--
-- Name: drafts_approvedcourses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_approvedcourses (
    id integer NOT NULL,
    comments character varying(300) NOT NULL,
    status boolean,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    course_draft_id_id integer NOT NULL,
    reason_rejected_id integer,
    user_id_id integer NOT NULL
);


ALTER TABLE drafts_approvedcourses OWNER TO postgres;

--
-- Name: drafts_approvedcourses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_approvedcourses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_approvedcourses_id_seq OWNER TO postgres;

--
-- Name: drafts_approvedcourses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_approvedcourses_id_seq OWNED BY drafts_approvedcourses.id;


--
-- Name: drafts_coursesroles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_coursesroles (
    id integer NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    course_draft_id_id integer NOT NULL,
    role_type_id integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE drafts_coursesroles OWNER TO postgres;

--
-- Name: drafts_coursesroles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_coursesroles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_coursesroles_id_seq OWNER TO postgres;

--
-- Name: drafts_coursesroles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_coursesroles_id_seq OWNED BY drafts_coursesroles.id;


--
-- Name: drafts_curriculumlecture; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_curriculumlecture (
    id integer NOT NULL,
    lecture_type character varying(20) NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(1500) NOT NULL,
    preview_url character varying(255),
    video_url character varying(255) NOT NULL,
    order_num integer NOT NULL,
    curriculum_section_id_id integer NOT NULL
);


ALTER TABLE drafts_curriculumlecture OWNER TO postgres;

--
-- Name: drafts_curriculumlecture_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_curriculumlecture_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_curriculumlecture_id_seq OWNER TO postgres;

--
-- Name: drafts_curriculumlecture_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_curriculumlecture_id_seq OWNED BY drafts_curriculumlecture.id;


--
-- Name: drafts_curriculumsection; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_curriculumsection (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    order_num integer NOT NULL,
    no_lectures integer NOT NULL,
    duration interval NOT NULL,
    course_draft_id_id integer NOT NULL
);


ALTER TABLE drafts_curriculumsection OWNER TO postgres;

--
-- Name: drafts_curriculumsection_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_curriculumsection_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_curriculumsection_id_seq OWNER TO postgres;

--
-- Name: drafts_curriculumsection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_curriculumsection_id_seq OWNED BY drafts_curriculumsection.id;


--
-- Name: drafts_draftcourse; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_draftcourse (
    id integer NOT NULL,
    title character varying(150) NOT NULL,
    subtitle character varying(250),
    ratings numeric(2,1),
    rating_count integer,
    students_enrolled integer,
    what_will_i_learn text,
    requirements text,
    description text,
    preview_video_url character varying(255),
    preview_image_url character varying(255),
    price numeric(9,2),
    discount numeric(9,2),
    no_lectures integer,
    no_hours numeric(5,1),
    slug character varying(50),
    label character varying(20),
    level character varying(20),
    created_at date NOT NULL,
    updated_at date NOT NULL,
    course_language_id integer,
    course_subcategory_id integer,
    is_draft boolean NOT NULL,
    is_reviewed boolean,
    status boolean
);


ALTER TABLE drafts_draftcourse OWNER TO postgres;

--
-- Name: drafts_draftcourse_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_draftcourse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_draftcourse_id_seq OWNER TO postgres;

--
-- Name: drafts_draftcourse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_draftcourse_id_seq OWNED BY drafts_draftcourse.id;


--
-- Name: drafts_draftcourse_instructor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_draftcourse_instructor (
    id integer NOT NULL,
    draftcourse_id integer NOT NULL,
    instructor_id integer NOT NULL
);


ALTER TABLE drafts_draftcourse_instructor OWNER TO postgres;

--
-- Name: drafts_draftcourse_instructor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_draftcourse_instructor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_draftcourse_instructor_id_seq OWNER TO postgres;

--
-- Name: drafts_draftcourse_instructor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_draftcourse_instructor_id_seq OWNED BY drafts_draftcourse_instructor.id;


--
-- Name: drafts_draftcourse_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_draftcourse_tags (
    id integer NOT NULL,
    draftcourse_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE drafts_draftcourse_tags OWNER TO postgres;

--
-- Name: drafts_draftcourse_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_draftcourse_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_draftcourse_tags_id_seq OWNER TO postgres;

--
-- Name: drafts_draftcourse_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_draftcourse_tags_id_seq OWNED BY drafts_draftcourse_tags.id;


--
-- Name: drafts_reasonsrejected; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_reasonsrejected (
    id integer NOT NULL,
    text character varying(100) NOT NULL,
    type character varying(20) NOT NULL
);


ALTER TABLE drafts_reasonsrejected OWNER TO postgres;

--
-- Name: drafts_reasonsrejected_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_reasonsrejected_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_reasonsrejected_id_seq OWNER TO postgres;

--
-- Name: drafts_reasonsrejected_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_reasonsrejected_id_seq OWNED BY drafts_reasonsrejected.id;


--
-- Name: drafts_reviewedcourses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE drafts_reviewedcourses (
    id integer NOT NULL,
    comments character varying(300) NOT NULL,
    status boolean,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    course_draft_id_id integer NOT NULL,
    reason_rejected_id integer,
    user_id_id integer NOT NULL
);


ALTER TABLE drafts_reviewedcourses OWNER TO postgres;

--
-- Name: drafts_reviewedcourses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE drafts_reviewedcourses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE drafts_reviewedcourses_id_seq OWNER TO postgres;

--
-- Name: drafts_reviewedcourses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE drafts_reviewedcourses_id_seq OWNED BY drafts_reviewedcourses.id;


--
-- Name: guroomed_inprogress; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE guroomed_inprogress (
    id integer NOT NULL,
    watching_video_duration interval NOT NULL,
    date_started timestamp with time zone NOT NULL,
    date_modified timestamp with time zone NOT NULL,
    courses_lecture_id_id integer NOT NULL
);


ALTER TABLE guroomed_inprogress OWNER TO root;

--
-- Name: guroomed_inprogress_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE guroomed_inprogress_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE guroomed_inprogress_id_seq OWNER TO root;

--
-- Name: guroomed_inprogress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE guroomed_inprogress_id_seq OWNED BY guroomed_inprogress.id;


--
-- Name: guroomed_notificationtypes; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE guroomed_notificationtypes (
    id integer NOT NULL,
    types character varying(150) NOT NULL
);


ALTER TABLE guroomed_notificationtypes OWNER TO root;

--
-- Name: guroomed_notificationtypes_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE guroomed_notificationtypes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE guroomed_notificationtypes_id_seq OWNER TO root;

--
-- Name: guroomed_notificationtypes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE guroomed_notificationtypes_id_seq OWNED BY guroomed_notificationtypes.id;


--
-- Name: guroomed_usercart; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE guroomed_usercart (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    course_id_id integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE guroomed_usercart OWNER TO postgres;

--
-- Name: guroomed_usercart_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE guroomed_usercart_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE guroomed_usercart_id_seq OWNER TO postgres;

--
-- Name: guroomed_usercart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE guroomed_usercart_id_seq OWNED BY guroomed_usercart.id;


--
-- Name: guroomed_usercourses; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE guroomed_usercourses (
    id integer NOT NULL,
    taught_learned character varying(8),
    is_favourite boolean NOT NULL,
    course_id_id integer NOT NULL,
    in_progress_id integer,
    user_id_id integer NOT NULL
);


ALTER TABLE guroomed_usercourses OWNER TO root;

--
-- Name: guroomed_usercourses_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE guroomed_usercourses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE guroomed_usercourses_id_seq OWNER TO root;

--
-- Name: guroomed_usercourses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE guroomed_usercourses_id_seq OWNED BY guroomed_usercourses.id;


--
-- Name: guroomed_userinfo; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE guroomed_userinfo (
    id integer NOT NULL,
    headline character varying(120),
    biography character varying(1600),
    website_link character varying(255),
    gplus_link character varying(50),
    twitter_link character varying(50),
    facebook_link character varying(50),
    linkedin_link character varying(50),
    youtube_link character varying(50),
    photo_link character varying(50),
    language_id integer,
    user_id_id integer NOT NULL,
    created_by_id integer
);


ALTER TABLE guroomed_userinfo OWNER TO root;

--
-- Name: guroomed_userinfo_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE guroomed_userinfo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE guroomed_userinfo_id_seq OWNER TO root;

--
-- Name: guroomed_userinfo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE guroomed_userinfo_id_seq OWNED BY guroomed_userinfo.id;


--
-- Name: guroomed_usernotification; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE guroomed_usernotification (
    id integer NOT NULL,
    notification_id_id integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE guroomed_usernotification OWNER TO root;

--
-- Name: guroomed_usernotification_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE guroomed_usernotification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE guroomed_usernotification_id_seq OWNER TO root;

--
-- Name: guroomed_usernotification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE guroomed_usernotification_id_seq OWNED BY guroomed_usernotification.id;


--
-- Name: guroomed_userprivacy; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE guroomed_userprivacy (
    id integer NOT NULL,
    hide_search_engine boolean NOT NULL,
    hide_courses boolean NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE guroomed_userprivacy OWNER TO root;

--
-- Name: guroomed_userprivacy_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE guroomed_userprivacy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE guroomed_userprivacy_id_seq OWNER TO root;

--
-- Name: guroomed_userprivacy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE guroomed_userprivacy_id_seq OWNED BY guroomed_userprivacy.id;


--
-- Name: homepage_footerstrip; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE homepage_footerstrip (
    id integer NOT NULL,
    title character varying(70) NOT NULL,
    description character varying(150) NOT NULL,
    url character varying(255) NOT NULL
);


ALTER TABLE homepage_footerstrip OWNER TO root;

--
-- Name: homepage_footerstrip_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE homepage_footerstrip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE homepage_footerstrip_id_seq OWNER TO root;

--
-- Name: homepage_footerstrip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE homepage_footerstrip_id_seq OWNED BY homepage_footerstrip.id;


--
-- Name: homepage_infostrip; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE homepage_infostrip (
    id integer NOT NULL,
    icon character varying(40) NOT NULL,
    title character varying(70) NOT NULL,
    subtitle character varying(100) NOT NULL
);


ALTER TABLE homepage_infostrip OWNER TO root;

--
-- Name: homepage_infostrip_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE homepage_infostrip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE homepage_infostrip_id_seq OWNER TO root;

--
-- Name: homepage_infostrip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE homepage_infostrip_id_seq OWNED BY homepage_infostrip.id;


--
-- Name: paywithpaypal_order; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE paywithpaypal_order (
    id integer NOT NULL,
    course_price numeric(9,2) NOT NULL,
    tax_price numeric(7,2) NOT NULL,
    discount_price numeric(7,2) NOT NULL,
    total_price numeric(9,2) NOT NULL,
    currency character varying(10) NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE paywithpaypal_order OWNER TO root;

--
-- Name: paywithpaypal_order_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE paywithpaypal_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE paywithpaypal_order_id_seq OWNER TO root;

--
-- Name: paywithpaypal_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE paywithpaypal_order_id_seq OWNED BY paywithpaypal_order.id;


--
-- Name: paywithpaypal_ordercourse; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE paywithpaypal_ordercourse (
    id integer NOT NULL,
    course_id_id integer NOT NULL,
    order_id_id integer NOT NULL,
    course_price numeric(9,2) NOT NULL
);


ALTER TABLE paywithpaypal_ordercourse OWNER TO postgres;

--
-- Name: paywithpaypal_ordercourse_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE paywithpaypal_ordercourse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE paywithpaypal_ordercourse_id_seq OWNER TO postgres;

--
-- Name: paywithpaypal_ordercourse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE paywithpaypal_ordercourse_id_seq OWNED BY paywithpaypal_ordercourse.id;


--
-- Name: paywithpaypal_payment; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE paywithpaypal_payment (
    id integer NOT NULL,
    course_price numeric(9,2),
    tax_price numeric(7,2),
    discount_price numeric(7,2),
    total_price numeric(9,2),
    currency character varying(10) NOT NULL,
    payment_status character varying(12) NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    order_id_id integer NOT NULL
);


ALTER TABLE paywithpaypal_payment OWNER TO root;

--
-- Name: paywithpaypal_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE paywithpaypal_payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE paywithpaypal_payment_id_seq OWNER TO root;

--
-- Name: paywithpaypal_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE paywithpaypal_payment_id_seq OWNED BY paywithpaypal_payment.id;


--
-- Name: paywithpaypal_paypaldetail; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE paywithpaypal_paypaldetail (
    id integer NOT NULL,
    payment_id character varying(100) NOT NULL,
    state character varying(30),
    cart character varying(30),
    payer_payment_method character varying(30),
    payer_status character varying(50),
    payer_email character varying(255),
    payer_id character varying(100),
    payer_country_code character varying(10),
    transactions_amount numeric(9,2),
    transactions_currency character varying(10),
    payee_merchant_id character varying(50),
    payee_email character varying(255),
    description character varying(500),
    payment_mode character varying(50),
    reason_code character varying(50),
    protection_eligibility character varying(50),
    transaction_fee numeric(5,2),
    created_at date,
    updated_at date,
    order_id_id integer NOT NULL
);


ALTER TABLE paywithpaypal_paypaldetail OWNER TO root;

--
-- Name: paywithpaypal_paypaldetail_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE paywithpaypal_paypaldetail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE paywithpaypal_paypaldetail_id_seq OWNER TO root;

--
-- Name: paywithpaypal_paypaldetail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE paywithpaypal_paypaldetail_id_seq OWNED BY paywithpaypal_paypaldetail.id;


--
-- Name: paywithpaypal_tax; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE paywithpaypal_tax (
    id integer NOT NULL,
    name character varying(30),
    description character varying(100),
    value numeric(5,2) NOT NULL
);


ALTER TABLE paywithpaypal_tax OWNER TO postgres;

--
-- Name: paywithpaypal_tax_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE paywithpaypal_tax_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE paywithpaypal_tax_id_seq OWNER TO postgres;

--
-- Name: paywithpaypal_tax_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE paywithpaypal_tax_id_seq OWNED BY paywithpaypal_tax.id;


--
-- Name: quizzes_answers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE quizzes_answers (
    id integer NOT NULL,
    answer character varying(500) NOT NULL,
    is_correct boolean NOT NULL,
    status boolean NOT NULL,
    "order" integer NOT NULL,
    question_id_id integer NOT NULL
);


ALTER TABLE quizzes_answers OWNER TO postgres;

--
-- Name: quizzes_answers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE quizzes_answers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE quizzes_answers_id_seq OWNER TO postgres;

--
-- Name: quizzes_answers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE quizzes_answers_id_seq OWNED BY quizzes_answers.id;


--
-- Name: quizzes_questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE quizzes_questions (
    id integer NOT NULL,
    content character varying(500) NOT NULL,
    status boolean NOT NULL,
    "order" integer NOT NULL,
    quiz_id_id integer NOT NULL,
    type_id_id integer NOT NULL
);


ALTER TABLE quizzes_questions OWNER TO postgres;

--
-- Name: quizzes_questions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE quizzes_questions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE quizzes_questions_id_seq OWNER TO postgres;

--
-- Name: quizzes_questions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE quizzes_questions_id_seq OWNED BY quizzes_questions.id;


--
-- Name: quizzes_questiontypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE quizzes_questiontypes (
    id integer NOT NULL,
    name character varying(70) NOT NULL
);


ALTER TABLE quizzes_questiontypes OWNER TO postgres;

--
-- Name: quizzes_questiontypes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE quizzes_questiontypes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE quizzes_questiontypes_id_seq OWNER TO postgres;

--
-- Name: quizzes_questiontypes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE quizzes_questiontypes_id_seq OWNED BY quizzes_questiontypes.id;


--
-- Name: quizzes_quizprogress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE quizzes_quizprogress (
    id integer NOT NULL,
    score integer NOT NULL,
    score_outof integer NOT NULL,
    status boolean NOT NULL,
    correct_questions character varying(500) NOT NULL,
    wrong_questions character varying(500) NOT NULL,
    skipped_questions character varying(500) NOT NULL,
    quiz_id_id integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE quizzes_quizprogress OWNER TO postgres;

--
-- Name: quizzes_quizprogress_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE quizzes_quizprogress_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE quizzes_quizprogress_id_seq OWNER TO postgres;

--
-- Name: quizzes_quizprogress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE quizzes_quizprogress_id_seq OWNED BY quizzes_quizprogress.id;


--
-- Name: quizzes_quizzes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE quizzes_quizzes (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(500),
    created_at date NOT NULL,
    course_section_id_id integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE quizzes_quizzes OWNER TO postgres;

--
-- Name: quizzes_quizzes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE quizzes_quizzes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE quizzes_quizzes_id_seq OWNER TO postgres;

--
-- Name: quizzes_quizzes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE quizzes_quizzes_id_seq OWNED BY quizzes_quizzes.id;


--
-- Name: social_auth_association; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE social_auth_association (
    id integer NOT NULL,
    server_url character varying(255) NOT NULL,
    handle character varying(255) NOT NULL,
    secret character varying(255) NOT NULL,
    issued integer NOT NULL,
    lifetime integer NOT NULL,
    assoc_type character varying(64) NOT NULL
);


ALTER TABLE social_auth_association OWNER TO root;

--
-- Name: social_auth_association_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE social_auth_association_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_association_id_seq OWNER TO root;

--
-- Name: social_auth_association_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE social_auth_association_id_seq OWNED BY social_auth_association.id;


--
-- Name: social_auth_code; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE social_auth_code (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    code character varying(32) NOT NULL,
    verified boolean NOT NULL,
    "timestamp" timestamp with time zone NOT NULL
);


ALTER TABLE social_auth_code OWNER TO root;

--
-- Name: social_auth_code_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE social_auth_code_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_code_id_seq OWNER TO root;

--
-- Name: social_auth_code_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE social_auth_code_id_seq OWNED BY social_auth_code.id;


--
-- Name: social_auth_nonce; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE social_auth_nonce (
    id integer NOT NULL,
    server_url character varying(255) NOT NULL,
    "timestamp" integer NOT NULL,
    salt character varying(65) NOT NULL
);


ALTER TABLE social_auth_nonce OWNER TO root;

--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE social_auth_nonce_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_nonce_id_seq OWNER TO root;

--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE social_auth_nonce_id_seq OWNED BY social_auth_nonce.id;


--
-- Name: social_auth_partial; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE social_auth_partial (
    id integer NOT NULL,
    token character varying(32) NOT NULL,
    next_step smallint NOT NULL,
    backend character varying(32) NOT NULL,
    data text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    CONSTRAINT social_auth_partial_next_step_check CHECK ((next_step >= 0))
);


ALTER TABLE social_auth_partial OWNER TO root;

--
-- Name: social_auth_partial_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE social_auth_partial_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_partial_id_seq OWNER TO root;

--
-- Name: social_auth_partial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE social_auth_partial_id_seq OWNED BY social_auth_partial.id;


--
-- Name: social_auth_usersocialauth; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE social_auth_usersocialauth (
    id integer NOT NULL,
    provider character varying(32) NOT NULL,
    uid character varying(255) NOT NULL,
    extra_data text NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE social_auth_usersocialauth OWNER TO root;

--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE social_auth_usersocialauth_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_usersocialauth_id_seq OWNER TO root;

--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE social_auth_usersocialauth_id_seq OWNED BY social_auth_usersocialauth.id;


--
-- Name: users_subcategoryroles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE users_subcategoryroles (
    id integer NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    role_type_id integer NOT NULL,
    subcategory_id_id integer NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE users_subcategoryroles OWNER TO postgres;

--
-- Name: users_subcategoryroles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE users_subcategoryroles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_subcategoryroles_id_seq OWNER TO postgres;

--
-- Name: users_subcategoryroles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE users_subcategoryroles_id_seq OWNED BY users_subcategoryroles.id;


--
-- Name: zenvimeo_item; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE zenvimeo_item (
    id integer NOT NULL,
    title character varying(200) NOT NULL,
    description text NOT NULL,
    video character varying(200) NOT NULL,
    video_group_id integer NOT NULL
);


ALTER TABLE zenvimeo_item OWNER TO root;

--
-- Name: zenvimeo_item_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE zenvimeo_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE zenvimeo_item_id_seq OWNER TO root;

--
-- Name: zenvimeo_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE zenvimeo_item_id_seq OWNED BY zenvimeo_item.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: courses_category id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_category ALTER COLUMN id SET DEFAULT nextval('courses_category_id_seq'::regclass);


--
-- Name: courses_course id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course ALTER COLUMN id SET DEFAULT nextval('courses_course_id_seq'::regclass);


--
-- Name: courses_course_instructor_id id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_course_instructor_id ALTER COLUMN id SET DEFAULT nextval('courses_course_instructor_id_id_seq'::regclass);


--
-- Name: courses_course_tags id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course_tags ALTER COLUMN id SET DEFAULT nextval('courses_course_tags_id_seq'::regclass);


--
-- Name: courses_curriculumlecture id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_curriculumlecture ALTER COLUMN id SET DEFAULT nextval('courses_curriculumlecture_id_seq'::regclass);


--
-- Name: courses_curriculumsection id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_curriculumsection ALTER COLUMN id SET DEFAULT nextval('courses_curriculumsection_id_seq'::regclass);


--
-- Name: courses_include id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_include ALTER COLUMN id SET DEFAULT nextval('courses_include_id_seq'::regclass);


--
-- Name: courses_instructor id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_instructor ALTER COLUMN id SET DEFAULT nextval('courses_instructor_id_seq'::regclass);


--
-- Name: courses_language id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_language ALTER COLUMN id SET DEFAULT nextval('courses_language_id_seq'::regclass);


--
-- Name: courses_studentreview id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_studentreview ALTER COLUMN id SET DEFAULT nextval('courses_studentreview_id_seq'::regclass);


--
-- Name: courses_studentreviewvote id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_studentreviewvote ALTER COLUMN id SET DEFAULT nextval('courses_studentreviewvote_id_seq'::regclass);


--
-- Name: courses_subcategory id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_subcategory ALTER COLUMN id SET DEFAULT nextval('courses_subcategory_id_seq'::regclass);


--
-- Name: courses_tag id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_tag ALTER COLUMN id SET DEFAULT nextval('courses_tag_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: drafts_approvedcourses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_approvedcourses ALTER COLUMN id SET DEFAULT nextval('drafts_approvedcourses_id_seq'::regclass);


--
-- Name: drafts_coursesroles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_coursesroles ALTER COLUMN id SET DEFAULT nextval('drafts_coursesroles_id_seq'::regclass);


--
-- Name: drafts_curriculumlecture id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_curriculumlecture ALTER COLUMN id SET DEFAULT nextval('drafts_curriculumlecture_id_seq'::regclass);


--
-- Name: drafts_curriculumsection id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_curriculumsection ALTER COLUMN id SET DEFAULT nextval('drafts_curriculumsection_id_seq'::regclass);


--
-- Name: drafts_draftcourse id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse ALTER COLUMN id SET DEFAULT nextval('drafts_draftcourse_id_seq'::regclass);


--
-- Name: drafts_draftcourse_instructor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_instructor ALTER COLUMN id SET DEFAULT nextval('drafts_draftcourse_instructor_id_seq'::regclass);


--
-- Name: drafts_draftcourse_tags id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_tags ALTER COLUMN id SET DEFAULT nextval('drafts_draftcourse_tags_id_seq'::regclass);


--
-- Name: drafts_reasonsrejected id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_reasonsrejected ALTER COLUMN id SET DEFAULT nextval('drafts_reasonsrejected_id_seq'::regclass);


--
-- Name: drafts_reviewedcourses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_reviewedcourses ALTER COLUMN id SET DEFAULT nextval('drafts_reviewedcourses_id_seq'::regclass);


--
-- Name: guroomed_inprogress id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_inprogress ALTER COLUMN id SET DEFAULT nextval('guroomed_inprogress_id_seq'::regclass);


--
-- Name: guroomed_notificationtypes id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_notificationtypes ALTER COLUMN id SET DEFAULT nextval('guroomed_notificationtypes_id_seq'::regclass);


--
-- Name: guroomed_usercart id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY guroomed_usercart ALTER COLUMN id SET DEFAULT nextval('guroomed_usercart_id_seq'::regclass);


--
-- Name: guroomed_usercourses id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usercourses ALTER COLUMN id SET DEFAULT nextval('guroomed_usercourses_id_seq'::regclass);


--
-- Name: guroomed_userinfo id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userinfo ALTER COLUMN id SET DEFAULT nextval('guroomed_userinfo_id_seq'::regclass);


--
-- Name: guroomed_usernotification id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usernotification ALTER COLUMN id SET DEFAULT nextval('guroomed_usernotification_id_seq'::regclass);


--
-- Name: guroomed_userprivacy id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userprivacy ALTER COLUMN id SET DEFAULT nextval('guroomed_userprivacy_id_seq'::regclass);


--
-- Name: homepage_footerstrip id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY homepage_footerstrip ALTER COLUMN id SET DEFAULT nextval('homepage_footerstrip_id_seq'::regclass);


--
-- Name: homepage_infostrip id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY homepage_infostrip ALTER COLUMN id SET DEFAULT nextval('homepage_infostrip_id_seq'::regclass);


--
-- Name: paywithpaypal_order id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_order ALTER COLUMN id SET DEFAULT nextval('paywithpaypal_order_id_seq'::regclass);


--
-- Name: paywithpaypal_ordercourse id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY paywithpaypal_ordercourse ALTER COLUMN id SET DEFAULT nextval('paywithpaypal_ordercourse_id_seq'::regclass);


--
-- Name: paywithpaypal_payment id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_payment ALTER COLUMN id SET DEFAULT nextval('paywithpaypal_payment_id_seq'::regclass);


--
-- Name: paywithpaypal_paypaldetail id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_paypaldetail ALTER COLUMN id SET DEFAULT nextval('paywithpaypal_paypaldetail_id_seq'::regclass);


--
-- Name: paywithpaypal_tax id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY paywithpaypal_tax ALTER COLUMN id SET DEFAULT nextval('paywithpaypal_tax_id_seq'::regclass);


--
-- Name: quizzes_answers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_answers ALTER COLUMN id SET DEFAULT nextval('quizzes_answers_id_seq'::regclass);


--
-- Name: quizzes_questions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_questions ALTER COLUMN id SET DEFAULT nextval('quizzes_questions_id_seq'::regclass);


--
-- Name: quizzes_questiontypes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_questiontypes ALTER COLUMN id SET DEFAULT nextval('quizzes_questiontypes_id_seq'::regclass);


--
-- Name: quizzes_quizprogress id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizprogress ALTER COLUMN id SET DEFAULT nextval('quizzes_quizprogress_id_seq'::regclass);


--
-- Name: quizzes_quizzes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizzes ALTER COLUMN id SET DEFAULT nextval('quizzes_quizzes_id_seq'::regclass);


--
-- Name: social_auth_association id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_association ALTER COLUMN id SET DEFAULT nextval('social_auth_association_id_seq'::regclass);


--
-- Name: social_auth_code id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_code ALTER COLUMN id SET DEFAULT nextval('social_auth_code_id_seq'::regclass);


--
-- Name: social_auth_nonce id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_nonce ALTER COLUMN id SET DEFAULT nextval('social_auth_nonce_id_seq'::regclass);


--
-- Name: social_auth_partial id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_partial ALTER COLUMN id SET DEFAULT nextval('social_auth_partial_id_seq'::regclass);


--
-- Name: social_auth_usersocialauth id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_usersocialauth ALTER COLUMN id SET DEFAULT nextval('social_auth_usersocialauth_id_seq'::regclass);


--
-- Name: users_subcategoryroles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users_subcategoryroles ALTER COLUMN id SET DEFAULT nextval('users_subcategoryroles_id_seq'::regclass);


--
-- Name: zenvimeo_item id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY zenvimeo_item ALTER COLUMN id SET DEFAULT nextval('zenvimeo_item_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_group (id, name) FROM stdin;
3	powerplant
4	compressors
1	Instructor
2	Student
5	Site Admin
6	Admin
7	Course Manager
8	Course Reviewer
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_group_id_seq', 8, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	97
2	1	98
3	1	99
4	1	100
5	2	100
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 5, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add association	7	add_association
20	Can change association	7	change_association
21	Can delete association	7	delete_association
22	Can add code	8	add_code
23	Can change code	8	change_code
24	Can delete code	8	delete_code
25	Can add nonce	9	add_nonce
26	Can change nonce	9	change_nonce
27	Can delete nonce	9	delete_nonce
28	Can add user social auth	10	add_usersocialauth
29	Can change user social auth	10	change_usersocialauth
30	Can delete user social auth	10	delete_usersocialauth
31	Can add partial	11	add_partial
32	Can change partial	11	change_partial
33	Can delete partial	11	delete_partial
34	Can add category	12	add_category
35	Can change category	12	change_category
36	Can delete category	12	delete_category
37	Can add subcategory	13	add_subcategory
38	Can change subcategory	13	change_subcategory
39	Can delete subcategory	13	delete_subcategory
40	Can add language	14	add_language
41	Can change language	14	change_language
42	Can delete language	14	delete_language
43	Can add instructor	15	add_instructor
44	Can change instructor	15	change_instructor
45	Can delete instructor	15	delete_instructor
46	Can add tag	16	add_tag
47	Can change tag	16	change_tag
48	Can delete tag	16	delete_tag
49	Can add course	17	add_course
50	Can change course	17	change_course
51	Can delete course	17	delete_course
52	Can add include	18	add_include
53	Can change include	18	change_include
54	Can delete include	18	delete_include
55	Can add curriculum section	19	add_curriculumsection
56	Can change curriculum section	19	change_curriculumsection
57	Can delete curriculum section	19	delete_curriculumsection
58	Can add curriculum lecture	20	add_curriculumlecture
59	Can change curriculum lecture	20	change_curriculumlecture
60	Can delete curriculum lecture	20	delete_curriculumlecture
61	Can add student review	21	add_studentreview
62	Can change student review	21	change_studentreview
63	Can delete student review	21	delete_studentreview
64	Can add user info	22	add_userinfo
65	Can change user info	22	change_userinfo
66	Can delete user info	22	delete_userinfo
67	Can add in progress	23	add_inprogress
68	Can change in progress	23	change_inprogress
69	Can delete in progress	23	delete_inprogress
70	Can add user courses	24	add_usercourses
71	Can change user courses	24	change_usercourses
72	Can delete user courses	24	delete_usercourses
73	Can add user privacy	25	add_userprivacy
74	Can change user privacy	25	change_userprivacy
75	Can delete user privacy	25	delete_userprivacy
76	Can add notification types	26	add_notificationtypes
77	Can change notification types	26	change_notificationtypes
78	Can delete notification types	26	delete_notificationtypes
79	Can add user notification	27	add_usernotification
80	Can change user notification	27	change_usernotification
81	Can delete user notification	27	delete_usernotification
82	Can add infostrip	28	add_infostrip
83	Can change infostrip	28	change_infostrip
84	Can delete infostrip	28	delete_infostrip
85	Can add footer strip	29	add_footerstrip
86	Can change footer strip	29	change_footerstrip
87	Can delete footer strip	29	delete_footerstrip
88	Can add order	30	add_order
89	Can change order	30	change_order
90	Can delete order	30	delete_order
91	Can add payment	31	add_payment
92	Can change payment	31	change_payment
93	Can delete payment	31	delete_payment
94	Can add paypal detail	32	add_paypaldetail
95	Can change paypal detail	32	change_paypaldetail
96	Can delete paypal detail	32	delete_paypaldetail
97	Can add item	33	add_item
98	Can change item	33	change_item
99	Can delete item	33	delete_item
100	Can view Videos in website	33	view_videos_ui
101	Can add student review vote	34	add_studentreviewvote
102	Can change student review vote	34	change_studentreviewvote
103	Can delete student review vote	34	delete_studentreviewvote
104	Can add user cart	35	add_usercart
105	Can change user cart	35	change_usercart
106	Can delete user cart	35	delete_usercart
107	Can add order course	36	add_ordercourse
108	Can change order course	36	change_ordercourse
109	Can delete order course	36	delete_ordercourse
110	Can add tax	37	add_tax
111	Can change tax	37	change_tax
112	Can delete tax	37	delete_tax
113	Can add email address	38	add_emailaddress
114	Can change email address	38	change_emailaddress
115	Can delete email address	38	delete_emailaddress
116	Can add draft course	39	add_draftcourse
117	Can change draft course	39	change_draftcourse
118	Can delete draft course	39	delete_draftcourse
119	Can add approved courses	40	add_approvedcourses
120	Can change approved courses	40	change_approvedcourses
121	Can delete approved courses	40	delete_approvedcourses
122	Can add courses roles	41	add_coursesroles
123	Can change courses roles	41	change_coursesroles
124	Can delete courses roles	41	delete_coursesroles
125	Can add reasons rejected	42	add_reasonsrejected
126	Can change reasons rejected	42	change_reasonsrejected
127	Can delete reasons rejected	42	delete_reasonsrejected
128	Can add reviewed courses	43	add_reviewedcourses
129	Can change reviewed courses	43	change_reviewedcourses
130	Can delete reviewed courses	43	delete_reviewedcourses
131	Can add curriculum lecture	44	add_curriculumlecture
132	Can change curriculum lecture	44	change_curriculumlecture
133	Can delete curriculum lecture	44	delete_curriculumlecture
134	Can add include	45	add_include
135	Can change include	45	change_include
136	Can delete include	45	delete_include
137	Can add curriculum section	46	add_curriculumsection
138	Can change curriculum section	46	change_curriculumsection
139	Can delete curriculum section	46	delete_curriculumsection
140	Can add subcategory roles	47	add_subcategoryroles
141	Can change subcategory roles	47	change_subcategoryroles
142	Can delete subcategory roles	47	delete_subcategoryroles
143	Can add answers	48	add_answers
144	Can change answers	48	change_answers
145	Can delete answers	48	delete_answers
146	Can add quiz progress	49	add_quizprogress
147	Can change quiz progress	49	change_quizprogress
148	Can delete quiz progress	49	delete_quizprogress
149	Can add questions	50	add_questions
150	Can change questions	50	change_questions
151	Can delete questions	50	delete_questions
152	Can add quizzes	51	add_quizzes
153	Can change quizzes	51	change_quizzes
154	Can delete quizzes	51	delete_quizzes
155	Can add question types	52	add_questiontypes
156	Can change question types	52	change_questiontypes
157	Can delete question types	52	delete_questiontypes
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_permission_id_seq', 157, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$100000$EKALCCSdlJmx$fsXEiug+Bbxdl8Wzfs3+atNeRzIZ5gcQPTsBCQFoob8=	2018-05-04 09:05:54.625541+05:30	t	admin	Admin	Guroomed	admin@guroomed.com	t	t	2018-01-29 12:08:07+05:30
43	pbkdf2_sha256$100000$0TdZ3gSPvvAZ$KRGqujqRgh4WQUtREhz5EOX8ao4wmF4UjBdeTZ3CcwE=	2018-05-04 09:51:19.117767+05:30	f	contact2amruta@gmail.com	Amruta	Karajagi	contact2amruta@gmail.com	f	t	2018-04-15 12:39:07+05:30
3	pbkdf2_sha256$100000$L63fUJm0X1g1$s+4yUTRjRnZBWi/gsgcjAgrjmgg5D13A5Yqy2U0w0mE=	2018-05-04 10:45:28.182309+05:30	f	coursemanager	CourseManager	Guroomed	coursemanager@guroomed.com	f	t	2018-02-07 10:45:53+05:30
39	pbkdf2_sha256$100000$i981ekVlTlBk$J+tqZ5P5ciXzKymD7hvbMVygcig+J4piHn4Drw125v8=	2018-04-28 15:13:40.445946+05:30	f	siteadmin	SiteAdmin	Guroomed	siteadmin@guroomed.com	f	t	2018-04-14 11:57:28+05:30
41	pbkdf2_sha256$100000$au86S9ifxI1P$qZvKgk5f8ftHnb9nfDVMIiCLgLQJ9sVNlE+9NwJhaPQ=	2018-04-30 18:47:52.051368+05:30	f	instructor	Instructor	Guroomed	instructor@guroomed.com	f	t	2018-04-14 12:00:10+05:30
40	pbkdf2_sha256$100000$o8le4AQLVNVy$bXsfwhlwIc0RcpF+V5C0QS2xThR8FHd6VW9/uKbhWYg=	2018-04-30 18:49:03.763968+05:30	f	coursereviewer	CourseReviewer	Guroomed	coursereviewer@guroomed.com	f	t	2018-04-14 11:58:58+05:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
9	1	1
10	1	2
11	1	3
12	1	4
27	1	8
28	1	5
29	1	6
30	1	7
31	3	7
32	39	5
33	40	8
34	41	1
68	43	2
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 76, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_id_seq', 80, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: courses_category; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_category (id, name) FROM stdin;
1	Development
2	Business
3	Design
\.


--
-- Name: courses_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_category_id_seq', 3, true);


--
-- Data for Name: courses_course; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_course (id, title, ratings, rating_count, students_enrolled, what_will_i_learn, requirements, description, preview_video_url, preview_image_url, price, discount, no_lectures, no_hours, level, created_at, updated_at, course_language_id_id, course_subcategory_id_id, subtitle, slug) FROM stdin;
91	test 6	\N	\N	\N	\N	\N	\N	\N	\N	1.00	\N	\N	\N	Expert	2018-05-04	2018-05-04	1	5	test 6 subtitle	\N
\.


--
-- Name: courses_course_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_course_id_seq', 91, true);


--
-- Data for Name: courses_course_instructor_id; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY courses_course_instructor_id (id, course_id, instructor_id) FROM stdin;
67	91	3
\.


--
-- Name: courses_course_instructor_id_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('courses_course_instructor_id_id_seq', 67, true);


--
-- Data for Name: courses_course_tags; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_course_tags (id, course_id, tag_id) FROM stdin;
\.


--
-- Name: courses_course_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_course_tags_id_seq', 49, true);


--
-- Data for Name: courses_curriculumlecture; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_curriculumlecture (id, title, description, preview_url, video_url, order_num, curriculum_section_id_id, lecture_type) FROM stdin;
\.


--
-- Name: courses_curriculumlecture_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_curriculumlecture_id_seq', 9, true);


--
-- Data for Name: courses_curriculumsection; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_curriculumsection (id, title, order_num, course_id_id, duration, no_lectures) FROM stdin;
\.


--
-- Name: courses_curriculumsection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_curriculumsection_id_seq', 9, true);


--
-- Data for Name: courses_include; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_include (id, hours_on_demand, supplemental_resources, lifetime_access, access_on_mobile, certificate, course_id_id) FROM stdin;
\.


--
-- Name: courses_include_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_include_id_seq', 1, false);


--
-- Data for Name: courses_instructor; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_instructor (id, rating, students, reviews, courses, user_id_id) FROM stdin;
3	4.3	3432412	7854	12	41
4	0.0	0	0	0	43
\.


--
-- Name: courses_instructor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_instructor_id_seq', 8, true);


--
-- Data for Name: courses_language; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_language (id, name) FROM stdin;
1	English
2	Spanish
3	Hindi
\.


--
-- Name: courses_language_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_language_id_seq', 3, true);


--
-- Data for Name: courses_studentreview; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_studentreview (id, no_of_stars, about_the_course, about_the_instructor, how_course_can_improved, review, course_id_id, user_id_id) FROM stdin;
\.


--
-- Name: courses_studentreview_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_studentreview_id_seq', 1, false);


--
-- Data for Name: courses_studentreviewvote; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY courses_studentreviewvote (id, "like", review_id_id, user_id_id) FROM stdin;
\.


--
-- Name: courses_studentreviewvote_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('courses_studentreviewvote_id_seq', 1, false);


--
-- Data for Name: courses_subcategory; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_subcategory (id, name, course_category_id_id) FROM stdin;
1	Game Development	1
2	Web Development	1
3	Finance	2
4	Operations	2
5	Web Design	3
6	Graphic Design	3
\.


--
-- Name: courses_subcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_subcategory_id_seq', 6, true);


--
-- Data for Name: courses_tag; Type: TABLE DATA; Schema: public; Owner: root
--

COPY courses_tag (id, name) FROM stdin;
1	PHP
3	Design
4	Python
5	Data Science
\.


--
-- Name: courses_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('courses_tag_id_seq', 5, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2018-01-29 12:12:39.279947+05:30	1	faculty	1	[{"added": {}}]	3	1
2	2018-01-29 12:13:05.125518+05:30	2	zen_student	1	[{"added": {}}]	3	1
3	2018-01-29 12:14:22.659649+05:30	3	powerplant	1	[{"added": {}}]	3	1
4	2018-01-29 12:15:32.157125+05:30	4	compressors	1	[{"added": {}}]	3	1
5	2018-01-29 12:42:49.897806+05:30	2	amruta	2	[]	4	1
6	2018-01-29 12:42:55.026295+05:30	1	admin	2	[]	4	1
7	2018-01-29 15:11:59.831905+05:30	1	Dummy Video	1	[{"added": {}}]	33	1
8	2018-01-29 16:28:26.46755+05:30	2	Dummy Video 1 Tittle	2	[{"changed": {"fields": ["video", "video_group"]}}]	33	1
9	2018-01-29 16:28:48.135917+05:30	1	Dummy Video 2 Tittle	2	[{"changed": {"fields": ["title", "description", "video", "video_group"]}}]	33	1
10	2018-01-29 16:29:10.809382+05:30	3	COUPLINGS	1	[{"added": {}}]	33	1
11	2018-03-08 14:28:43.865461+05:30	1	admin	2	[{"changed": {"fields": ["groups"]}}]	4	1
12	2018-03-08 14:29:43.384257+05:30	6	zenrays	2	[{"changed": {"fields": ["username", "email", "groups"]}}]	4	1
13	2018-04-09 11:20:41.715464+05:30	1	Instructor	2	[{"changed": {"fields": ["name"]}}]	3	1
14	2018-04-09 11:20:58.086856+05:30	2	Student	2	[{"changed": {"fields": ["name"]}}]	3	1
15	2018-04-14 04:32:21.231087+05:30	5	Site Admin	1	[{"added": {}}]	3	1
16	2018-04-14 04:32:28.038314+05:30	6	Admin	1	[{"added": {}}]	3	1
17	2018-04-14 04:32:53.011342+05:30	7	Course Manager	1	[{"added": {}}]	3	1
18	2018-04-14 04:33:07.596791+05:30	8	Course Reviewer	1	[{"added": {}}]	3	1
19	2018-04-14 11:54:12.946344+05:30	38	zenrays.amruta@gmail.com	2	[{"changed": {"fields": ["first_name", "last_name", "is_active", "is_staff", "is_superuser", "groups"]}}]	4	1
20	2018-04-14 11:54:29.157636+05:30	1	admin	2	[{"changed": {"fields": ["groups"]}}]	4	1
21	2018-04-14 11:55:38.585376+05:30	1	admin	2	[{"changed": {"fields": ["first_name", "last_name"]}}]	4	1
22	2018-04-14 11:56:31.664549+05:30	3	coursemanager@guroomed.com	2	[{"changed": {"fields": ["username", "first_name", "last_name", "email", "groups"]}}]	4	1
23	2018-04-14 11:57:28.561715+05:30	39	siteadmin	1	[{"added": {}}]	4	1
24	2018-04-14 11:57:56.923709+05:30	39	siteadmin	2	[{"changed": {"fields": ["first_name", "last_name", "email", "groups"]}}]	4	1
25	2018-04-14 11:58:17.397602+05:30	3	coursemanager	2	[{"changed": {"fields": ["username"]}}]	4	1
26	2018-04-14 11:58:58.516819+05:30	40	coursereviewer	1	[{"added": {}}]	4	1
27	2018-04-14 11:59:23.710544+05:30	40	coursereviewer	2	[{"changed": {"fields": ["first_name", "last_name", "email", "groups"]}}]	4	1
28	2018-04-14 12:00:11.044987+05:30	41	instructor	1	[{"added": {}}]	4	1
29	2018-04-14 12:00:34.919654+05:30	41	instructor	2	[{"changed": {"fields": ["first_name", "last_name", "email", "groups"]}}]	4	1
30	2018-04-16 17:28:17.951976+05:30	44	zenrays.amruta@gmail.comq	2	[{"changed": {"fields": ["username"]}}]	4	1
31	2018-04-20 12:45:37.215136+05:30	50	coursereviewer2	1	[{"added": {}}]	4	1
32	2018-04-20 12:46:49.864827+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
33	2018-04-20 12:48:18.628778+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups"]}}]	4	1
34	2018-04-20 12:48:50.000045+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups"]}}]	4	1
35	2018-04-20 12:54:26.93715+05:30	51	coursereviewer3	1	[{"added": {}}]	4	1
36	2018-04-20 12:54:36.811395+05:30	51	coursereviewer3	2	[{"changed": {"fields": ["groups"]}}]	4	1
37	2018-04-23 12:02:07.420315+05:30	43	contact2amruta@gmail.com	2	[{"changed": {"fields": ["groups"]}}]	4	1
38	2018-04-23 12:02:16.978551+05:30	40	coursereviewer	2	[{"changed": {"fields": ["groups"]}}]	4	1
39	2018-04-23 12:02:23.501293+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups"]}}]	4	1
40	2018-04-23 12:02:33.647254+05:30	49	zenrays.amruta@gmail.com	2	[{"changed": {"fields": ["groups"]}}]	4	1
41	2018-04-23 12:02:46.546722+05:30	44	zenrays.amruta@gmail.comq	2	[{"changed": {"fields": ["groups"]}}]	4	1
42	2018-04-23 12:08:55.095121+05:30	49	zenrays.amruta@gmail.com	2	[{"changed": {"fields": ["password"]}}]	4	1
43	2018-04-23 12:11:35.878273+05:30	49	zenrays.amruta@gmail.com	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
44	2018-04-23 12:12:07.057983+05:30	44	zenrays.amruta@gmail.comq	2	[{"changed": {"fields": ["groups"]}}]	4	1
45	2018-04-23 12:15:41.200114+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
46	2018-04-23 12:16:47.077808+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups"]}}]	4	1
47	2018-04-23 12:17:02.215799+05:30	40	coursereviewer	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
48	2018-04-23 12:18:33.037029+05:30	43	contact2amruta@gmail.com	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
49	2018-04-23 12:26:10.425447+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups"]}}]	4	1
50	2018-04-23 12:27:15.041217+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups"]}}]	4	1
51	2018-04-23 12:27:29.680471+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
52	2018-04-23 12:27:50.931122+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups"]}}]	4	1
53	2018-04-23 12:28:03.051769+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
54	2018-04-23 12:28:20.713257+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
55	2018-04-23 12:28:39.326301+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
56	2018-04-23 12:30:13.341426+05:30	50	coursereviewer2	2	[{"changed": {"fields": ["groups", "last_login"]}}]	4	1
57	2018-04-24 09:55:07.514204+05:30	53	abc@gmail.com	3		4	1
58	2018-04-24 09:55:07.522207+05:30	54	abc1@gmail.com	3		4	1
59	2018-04-24 09:55:07.522207+05:30	55	abc11@gmail.com	3		4	1
60	2018-04-24 09:55:07.526207+05:30	52	condsfa@gmail.com	3		4	1
61	2018-04-26 11:57:52.175398+05:30	63	amruta1@zenrays.com	2	[{"changed": {"fields": ["is_active"]}}]	4	1
62	2018-04-26 11:57:58.240771+05:30	64	amruta2@zenrays.com	2	[{"changed": {"fields": ["is_active"]}}]	4	1
63	2018-04-26 12:05:50.772063+05:30	62	afsda@test.com	3		4	1
64	2018-04-26 12:05:50.778066+05:30	63	amruta1@zenrays.com	3		4	1
65	2018-04-26 12:05:50.781568+05:30	64	amruta2@zenrays.com	3		4	1
66	2018-04-26 12:06:37.497144+05:30	50	coursereviewer2	3		4	1
67	2018-04-26 12:07:07.709798+05:30	49	zenrays.amruta@gmail.com	3		4	1
68	2018-04-26 12:07:44.567987+05:30	44	zenrays.amruta@gmail.comq	3		4	1
69	2018-04-26 12:08:06.391013+05:30	43	contact2amruta@gmail.com	2	[{"changed": {"fields": ["groups"]}}]	4	1
70	2018-04-26 14:51:48.605758+05:30	67	abc@guroomed.com	3		4	1
71	2018-04-26 14:51:48.611762+05:30	70	abc@guroomed.com1	3		4	1
72	2018-04-26 14:51:48.615765+05:30	72	abc@guroomed.com2	3		4	1
73	2018-04-26 14:51:48.618769+05:30	74	abc1@guroomed.com	3		4	1
74	2018-04-26 14:51:48.622778+05:30	69	abc111@guroomed.com	3		4	1
75	2018-04-26 14:51:48.626775+05:30	68	admin1@guroomed.com	3		4	1
76	2018-04-26 14:51:48.629784+05:30	66	amruta1@zenrays.com	3		4	1
77	2018-04-26 14:51:48.634778+05:30	65	manager1@gmail.com	3		4	1
78	2018-04-28 16:18:11.410183+05:30	76	admin1@funstay.in	3		4	1
79	2018-04-28 16:18:11.528057+05:30	78	ba1c@gmail.com	3		4	1
80	2018-04-28 16:18:11.600103+05:30	77	bac@gmail.com	3		4	1
81	2018-04-28 16:18:11.601617+05:30	75	manager1@guroomed.com	3		4	1
82	2018-04-28 16:18:11.603107+05:30	79	xyz@test.com	3		4	1
83	2018-04-28 16:18:11.604107+05:30	80	xyz1@test.com	3		4	1
84	2018-04-28 16:18:46.788352+05:30	5	test	3		33	1
85	2018-04-28 16:18:46.791352+05:30	4	best mobile apps course	3		33	1
86	2018-04-28 16:18:46.792853+05:30	3	COUPLINGS	3		33	1
87	2018-04-28 16:18:46.794354+05:30	2	Dummy Video 1 Tittle	3		33	1
88	2018-04-28 16:18:46.795855+05:30	1	Dummy Video 2 Tittle	3		33	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 88, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	social_django	association
8	social_django	code
9	social_django	nonce
10	social_django	usersocialauth
11	social_django	partial
12	courses	category
13	courses	subcategory
14	courses	language
15	courses	instructor
16	courses	tag
17	courses	course
18	courses	include
19	courses	curriculumsection
20	courses	curriculumlecture
21	courses	studentreview
22	guroomed	userinfo
23	guroomed	inprogress
24	guroomed	usercourses
25	guroomed	userprivacy
26	guroomed	notificationtypes
27	guroomed	usernotification
28	homepage	infostrip
29	homepage	footerstrip
30	paywithpaypal	order
31	paywithpaypal	payment
32	paywithpaypal	paypaldetail
33	zenvimeo	item
34	courses	studentreviewvote
35	guroomed	usercart
36	paywithpaypal	ordercourse
37	paywithpaypal	tax
38	simple_email_confirmation	emailaddress
39	drafts	draftcourse
40	drafts	approvedcourses
41	drafts	coursesroles
42	drafts	reasonsrejected
43	drafts	reviewedcourses
44	drafts	curriculumlecture
45	drafts	include
46	drafts	curriculumsection
47	users	subcategoryroles
48	quizzes	answers
49	quizzes	quizprogress
50	quizzes	questions
51	quizzes	quizzes
52	quizzes	questiontypes
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_content_type_id_seq', 52, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-01-29 11:35:34.188756+05:30
2	auth	0001_initial	2018-01-29 11:35:34.548361+05:30
3	admin	0001_initial	2018-01-29 11:35:34.673364+05:30
4	admin	0002_logentry_remove_auto_add	2018-01-29 11:35:34.704612+05:30
5	contenttypes	0002_remove_content_type_name	2018-01-29 11:35:34.897505+05:30
6	auth	0002_alter_permission_name_max_length	2018-01-29 11:35:34.944378+05:30
7	auth	0003_alter_user_email_max_length	2018-01-29 11:35:35.053756+05:30
8	auth	0004_alter_user_username_opts	2018-01-29 11:35:35.100634+05:30
9	auth	0005_alter_user_last_login_null	2018-01-29 11:35:35.147506+05:30
10	auth	0006_require_contenttypes_0002	2018-01-29 11:35:35.163132+05:30
11	auth	0007_alter_validators_add_error_messages	2018-01-29 11:35:35.194379+05:30
12	auth	0008_alter_user_username_max_length	2018-01-29 11:35:35.272508+05:30
13	sessions	0001_initial	2018-01-29 11:35:35.350633+05:30
14	default	0001_initial	2018-01-29 11:35:35.663137+05:30
15	social_auth	0001_initial	2018-01-29 11:35:35.663137+05:30
16	default	0002_add_related_name	2018-01-29 11:35:35.741262+05:30
17	social_auth	0002_add_related_name	2018-01-29 11:35:35.756889+05:30
18	default	0003_alter_email_max_length	2018-01-29 11:35:35.78814+05:30
19	social_auth	0003_alter_email_max_length	2018-01-29 11:35:35.78814+05:30
20	default	0004_auto_20160423_0400	2018-01-29 11:35:35.835012+05:30
21	social_auth	0004_auto_20160423_0400	2018-01-29 11:35:35.835012+05:30
22	social_auth	0005_auto_20160727_2333	2018-01-29 11:35:35.875687+05:30
23	social_django	0006_partial	2018-01-29 11:35:35.93819+05:30
24	social_django	0003_alter_email_max_length	2018-01-29 11:35:35.953813+05:30
25	social_django	0001_initial	2018-01-29 11:35:35.953813+05:30
26	social_django	0004_auto_20160423_0400	2018-01-29 11:35:35.953813+05:30
27	social_django	0005_auto_20160727_2333	2018-01-29 11:35:35.969438+05:30
28	social_django	0002_add_related_name	2018-01-29 11:35:35.969438+05:30
29	courses	0001_initial	2018-01-29 12:05:11.459555+05:30
30	guroomed	0001_initial	2018-01-29 12:05:12.178311+05:30
31	homepage	0001_initial	2018-01-29 12:05:12.240997+05:30
32	paywithpaypal	0001_initial	2018-01-29 12:05:12.678501+05:30
33	zenvimeo	0001_initial	2018-01-29 12:05:12.834753+05:30
34	courses	0002_auto_20180213_0601	2018-02-13 06:06:52.02856+05:30
35	courses	0003_auto_20180213_1613	2018-02-13 16:14:21.353723+05:30
36	guroomed	0002_auto_20180213_1613	2018-02-13 16:14:21.416226+05:30
37	guroomed	0003_usercart	2018-02-16 02:13:23.82283+05:30
38	paywithpaypal	0002_auto_20180226_1738	2018-02-26 17:38:47.515232+05:30
39	paywithpaypal	0003_ordercourse_course_price	2018-02-26 19:24:56.758093+05:30
40	auth	0009_alter_user_last_name_max_length	2018-02-28 16:13:43.868633+05:30
41	social_django	0007_code_timestamp	2018-02-28 16:13:44.284821+05:30
42	social_django	0008_partial_timestamp	2018-02-28 16:13:44.377386+05:30
43	paywithpaypal	0004_tax	2018-03-05 16:01:51.652579+05:30
44	paywithpaypal	0005_auto_20180305_1645	2018-03-05 16:45:40.1188+05:30
45	courses	0004_auto_20180306_1831	2018-03-06 18:31:30.469642+05:30
46	courses	0005_auto_20180308_1221	2018-03-08 12:21:10.871172+05:30
47	courses	0006_auto_20180308_1836	2018-03-08 18:36:46.788392+05:30
48	courses	0007_auto_20180309_1206	2018-03-09 12:06:55.617983+05:30
49	courses	0008_auto_20180315_1003	2018-03-15 10:07:18.36328+05:30
50	courses	0009_curriculumlecture_lecture_type	2018-04-03 13:09:01.76778+05:30
52	courses	0010_auto_20180414_0330	2018-04-14 03:30:29.002586+05:30
53	drafts	0001_initial	2018-04-14 03:30:29.77186+05:30
54	drafts	0002_auto_20180414_1132	2018-04-14 11:33:52.428352+05:30
55	drafts	0003_auto_20180415_0743	2018-04-15 07:43:42.183982+05:30
56	drafts	0004_auto_20180415_1611	2018-04-15 16:11:21.20839+05:30
57	drafts	0005_auto_20180415_1612	2018-04-15 16:12:19.703789+05:30
58	courses	0011_auto_20180416_1810	2018-04-16 18:10:38.630361+05:30
59	drafts	0006_auto_20180416_1810	2018-04-16 18:10:38.993138+05:30
60	drafts	0007_auto_20180418_1304	2018-04-18 13:04:40.969944+05:30
61	drafts	0008_auto_20180421_1208	2018-04-24 10:55:54.044535+05:30
62	users	0001_initial	2018-04-24 10:55:54.273342+05:30
63	guroomed	0004_auto_20180428_1101	2018-04-28 11:01:35.539171+05:30
64	quizzes	0001_initial	2018-05-20 14:52:48.16463+05:30
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_migrations_id_seq', 64, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
ckeoqwcfso640drht6ai195ubhfx8dx8	YzFkZTNiNzg3NjA4NmJlMTI2OTdmZGMzMzNlZjRiOWJiOTU3NjQ5NDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYTk0YWJjN2UzMThkNDU2Y2Q5NzEzZWQzMmRkMGEwMGIyMmEyMDMzIn0=	2018-03-12 11:50:04.757761+05:30
gs9dnk44g5uget9yn3229pk44lcawz3n	MDFhOTQ4NjE1ODQwOTU4NWRmNDRmZDNkZjkzZTMwMWMzNTJjYTNiMjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDYxYWViZmE0M2RkNzEzN2Y3NWE4NjAyMmI4OGYzNzk1Yjc4MDliIn0=	2018-02-22 10:00:36.646727+05:30
bhg2lt36l6oi908onu8td5efgwmg9lk3	ODI0ZjU5YThlYTg3MTAzNGQxMmNkMWY5N2E3MzEwZjQyNTY3ZjIxMTp7Il9hdXRoX3VzZXJfaWQiOiI1NyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiM2FlN2IyNzQ3YTdjMWEyYTQ2ZDc1YzI5MDJlODEwNGNiNWU3ZmVhMiJ9	2018-05-08 10:20:05.041642+05:30
wp6va9tq8g8bzlte2ky83gyeocjgf8at	OWQ3MTgwOTAzMTgwZmQwYzM1OTI3ZDNjMGNmNzcyNTlkZDkxYmZkZDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDIwMDE5MGQzMTAxOWI1Yzc4NmQxMDAyMWMyNWY2MTZhNWMzNzVkIn0=	2018-05-18 09:02:19.048395+05:30
8b67w7g49lc62n28uwc0zdyoer1ayv6s	NjA2OTVjMGYxMjhlNzM5NTgyZjA0YzFmYzhhOWM4OTMyNWE3MzU3ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjMWUzMmRjOWQzNGQ3YjNiYjgwMzRlMzlmYjQ0MzUzYjY5OTQ2NzlkIn0=	2018-03-28 17:00:27.2767+05:30
7bxu9n4hjhpu2nma7ddb8q5cccci9q14	NzkxNDYxMmEwNGRmYTBhZTEzZjZiN2QxODM1MjQ5NzUwNWFjYWMxYzp7Il9hdXRoX3VzZXJfaWQiOiI0MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjMzMzZiY2NhYmQ2Y2NmNWM2OWJhNTlkNTllMjhlOGZmMTEyZjc4OCJ9	2018-05-08 11:34:56.346066+05:30
u8du3eyoood8hedvh5ydcyenhntj1vjj	NmE4ZTY2ODI0MDNlZjdhMTRmMmEyMjU3NWM2YzkyZTU0NzA1ZjE0Mjp7fQ==	2018-02-22 19:01:32.474828+05:30
vij2ons8txewfhyanoduai1ekiarq6p5	OWQ3MTgwOTAzMTgwZmQwYzM1OTI3ZDNjMGNmNzcyNTlkZDkxYmZkZDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDIwMDE5MGQzMTAxOWI1Yzc4NmQxMDAyMWMyNWY2MTZhNWMzNzVkIn0=	2018-05-18 10:45:28.182309+05:30
9v7ss4faoj6jeahnsnhawfq72kyj0nq1	NmE4ZTY2ODI0MDNlZjdhMTRmMmEyMjU3NWM2YzkyZTU0NzA1ZjE0Mjp7fQ==	2018-04-24 18:32:11.807888+05:30
qye0ok4f3o03ezses6rlnp3u6c18cf0n	MWY1YzFlNGFjMjZiMjMyNzc3NWRiNjg5NGM0NjljMjJlOTgyY2JhOTp7Il9hdXRoX3VzZXJfaWQiOiI3NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDE4NzY2MTdkOWZhYmQ1NmIwYTIzYTkxNGEzZWZkOGYwZGY0MTRjYSJ9	2018-05-10 15:15:23.551277+05:30
xjanxkaobfvknashd0elzsm95sfq0y60	NjA2OTVjMGYxMjhlNzM5NTgyZjA0YzFmYzhhOWM4OTMyNWE3MzU3ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjMWUzMmRjOWQzNGQ3YjNiYjgwMzRlMzlmYjQ0MzUzYjY5OTQ2NzlkIn0=	2018-04-29 11:13:38.056963+05:30
\.


--
-- Data for Name: drafts_approvedcourses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_approvedcourses (id, comments, status, created_at, updated_at, course_draft_id_id, reason_rejected_id, user_id_id) FROM stdin;
1		f	2018-04-20	2018-04-20	1	6	3
2		f	2018-04-20	2018-04-20	1	6	3
3		f	2018-04-20	2018-04-20	1	6	3
4		t	2018-04-20	2018-04-20	1	\N	3
5		t	2018-04-20	2018-04-20	1	\N	3
7		f	2018-04-20	2018-04-20	1	6	3
13		t	2018-04-20	2018-04-20	5	\N	3
14		t	2018-04-20	2018-04-20	5	\N	3
16	dsfads fdsa fa dsf ads	t	2018-05-04	2018-05-04	12	\N	3
\.


--
-- Name: drafts_approvedcourses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_approvedcourses_id_seq', 16, true);


--
-- Data for Name: drafts_coursesroles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_coursesroles (id, created_at, updated_at, course_draft_id_id, role_type_id, user_id_id) FROM stdin;
\.


--
-- Name: drafts_coursesroles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_coursesroles_id_seq', 23, true);


--
-- Data for Name: drafts_curriculumlecture; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_curriculumlecture (id, lecture_type, title, description, preview_url, video_url, order_num, curriculum_section_id_id) FROM stdin;
\.


--
-- Name: drafts_curriculumlecture_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_curriculumlecture_id_seq', 1, false);


--
-- Data for Name: drafts_curriculumsection; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_curriculumsection (id, title, order_num, no_lectures, duration, course_draft_id_id) FROM stdin;
\.


--
-- Name: drafts_curriculumsection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_curriculumsection_id_seq', 1, false);


--
-- Data for Name: drafts_draftcourse; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_draftcourse (id, title, subtitle, ratings, rating_count, students_enrolled, what_will_i_learn, requirements, description, preview_video_url, preview_image_url, price, discount, no_lectures, no_hours, slug, label, level, created_at, updated_at, course_language_id, course_subcategory_id, is_draft, is_reviewed, status) FROM stdin;
2	test	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-14	2018-04-14	\N	\N	t	\N	\N
4	test	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-14	2018-04-14	\N	\N	t	\N	\N
6	test6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-15	2018-04-15	\N	\N	t	\N	\N
7	test6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-15	2018-04-15	\N	\N	t	\N	\N
8	test6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-15	2018-04-15	\N	\N	t	\N	\N
9	test6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-15	2018-04-15	\N	\N	t	\N	\N
10	test6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-15	2018-04-15	\N	\N	t	\N	\N
11	test6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-04-15	2018-04-15	\N	\N	t	\N	\N
1	test 1	test 1 subtitle	\N	\N	\N	\N	\N	\N	\N	\N	12.00	\N	\N	\N	\N	New	Expert	2018-04-28	2018-04-28	1	5	t	t	\N
5	test 5	course_subtitle 5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	Beginner	2018-04-28	2018-04-28	3	3	t	f	t
3	test	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	New	All	2018-05-04	2018-05-04	\N	\N	t	\N	\N
12	test 6	test 6 subtitle	\N	\N	\N	\N	\N	\N	\N	\N	1.00	\N	\N	\N	\N	New	Expert	2018-05-04	2018-05-04	1	5	t	f	t
\.


--
-- Name: drafts_draftcourse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_draftcourse_id_seq', 12, true);


--
-- Data for Name: drafts_draftcourse_instructor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_draftcourse_instructor (id, draftcourse_id, instructor_id) FROM stdin;
4	4	3
5	5	3
6	6	3
12	12	3
\.


--
-- Name: drafts_draftcourse_instructor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_draftcourse_instructor_id_seq', 12, true);


--
-- Data for Name: drafts_draftcourse_tags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_draftcourse_tags (id, draftcourse_id, tag_id) FROM stdin;
\.


--
-- Name: drafts_draftcourse_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_draftcourse_tags_id_seq', 1, false);


--
-- Data for Name: drafts_reasonsrejected; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_reasonsrejected (id, text, type) FROM stdin;
1	Video Quality is blur	Course Manager
2	Video Content is not appropriate	Course Manager
3	Some of the topics are repeating	Course Manager
4	Teaching Quality is not as per Guroomed standard	Course Manager
5	Video Quality is blur	Course Reviewer
7	Some of the topics are repeating	Course Reviewer
8	Teaching Quality is not as per Guroomed standard	Course Reviewer
6	Video Content is not appropriate	Course Reviewer
\.


--
-- Name: drafts_reasonsrejected_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_reasonsrejected_id_seq', 8, true);


--
-- Data for Name: drafts_reviewedcourses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY drafts_reviewedcourses (id, comments, status, created_at, updated_at, course_draft_id_id, reason_rejected_id, user_id_id) FROM stdin;
7		t	2018-04-20	2018-04-20	1	\N	40
8		t	2018-04-20	2018-04-20	1	\N	40
\.


--
-- Name: drafts_reviewedcourses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('drafts_reviewedcourses_id_seq', 9, true);


--
-- Data for Name: guroomed_inprogress; Type: TABLE DATA; Schema: public; Owner: root
--

COPY guroomed_inprogress (id, watching_video_duration, date_started, date_modified, courses_lecture_id_id) FROM stdin;
\.


--
-- Name: guroomed_inprogress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('guroomed_inprogress_id_seq', 1, false);


--
-- Data for Name: guroomed_notificationtypes; Type: TABLE DATA; Schema: public; Owner: root
--

COPY guroomed_notificationtypes (id, types) FROM stdin;
\.


--
-- Name: guroomed_notificationtypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('guroomed_notificationtypes_id_seq', 1, false);


--
-- Data for Name: guroomed_usercart; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY guroomed_usercart (id, created_at, updated_at, course_id_id, user_id_id) FROM stdin;
\.


--
-- Name: guroomed_usercart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('guroomed_usercart_id_seq', 89, true);


--
-- Data for Name: guroomed_usercourses; Type: TABLE DATA; Schema: public; Owner: root
--

COPY guroomed_usercourses (id, taught_learned, is_favourite, course_id_id, in_progress_id, user_id_id) FROM stdin;
\.


--
-- Name: guroomed_usercourses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('guroomed_usercourses_id_seq', 23, true);


--
-- Data for Name: guroomed_userinfo; Type: TABLE DATA; Schema: public; Owner: root
--

COPY guroomed_userinfo (id, headline, biography, website_link, gplus_link, twitter_link, facebook_link, linkedin_link, youtube_link, photo_link, language_id, user_id_id, created_by_id) FROM stdin;
2									/media/Php_64.jpg	\N	1	\N
\.


--
-- Name: guroomed_userinfo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('guroomed_userinfo_id_seq', 7, true);


--
-- Data for Name: guroomed_usernotification; Type: TABLE DATA; Schema: public; Owner: root
--

COPY guroomed_usernotification (id, notification_id_id, user_id_id) FROM stdin;
\.


--
-- Name: guroomed_usernotification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('guroomed_usernotification_id_seq', 1, false);


--
-- Data for Name: guroomed_userprivacy; Type: TABLE DATA; Schema: public; Owner: root
--

COPY guroomed_userprivacy (id, hide_search_engine, hide_courses, user_id_id) FROM stdin;
\.


--
-- Name: guroomed_userprivacy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('guroomed_userprivacy_id_seq', 1, false);


--
-- Data for Name: homepage_footerstrip; Type: TABLE DATA; Schema: public; Owner: root
--

COPY homepage_footerstrip (id, title, description, url) FROM stdin;
1	Become an Instructor	Teach what you love. Guroomed gives you the tools to create an online course.	#
2	Guroomed for Business	Get unlimited access to 2,000 of GuroomedΓÇÖs top courses for your team.	#
\.


--
-- Name: homepage_footerstrip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('homepage_footerstrip_id_seq', 3, true);


--
-- Data for Name: homepage_infostrip; Type: TABLE DATA; Schema: public; Owner: root
--

COPY homepage_infostrip (id, icon, title, subtitle) FROM stdin;
1	fa-external-link	55,000 online courses	Explore a variety of fresh topics
2	fa-check	Expert Instruction	Find the right instructor for you
3	fa-clock-o	Lifetime Access	Learn on your schedule
\.


--
-- Name: homepage_infostrip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('homepage_infostrip_id_seq', 8, true);


--
-- Data for Name: paywithpaypal_order; Type: TABLE DATA; Schema: public; Owner: root
--

COPY paywithpaypal_order (id, course_price, tax_price, discount_price, total_price, currency, created_at, updated_at, user_id_id) FROM stdin;
12	15000.00	15.00	12000.00	3015.00	INR	2018-03-14	2018-03-14	1
13	2343.00	10.15	313.00	2040.15	INR	2018-03-15	2018-03-15	1
14	2343.00	10.15	313.00	2040.15	INR	2018-03-15	2018-03-15	1
\.


--
-- Name: paywithpaypal_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('paywithpaypal_order_id_seq', 14, true);


--
-- Data for Name: paywithpaypal_ordercourse; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY paywithpaypal_ordercourse (id, course_id_id, order_id_id, course_price) FROM stdin;
\.


--
-- Name: paywithpaypal_ordercourse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('paywithpaypal_ordercourse_id_seq', 8, true);


--
-- Data for Name: paywithpaypal_payment; Type: TABLE DATA; Schema: public; Owner: root
--

COPY paywithpaypal_payment (id, course_price, tax_price, discount_price, total_price, currency, payment_status, created_at, updated_at, order_id_id) FROM stdin;
12	15000.00	15.00	12000.00	3015.00	INR	successful	2018-03-14	2018-03-14	12
13	2343.00	10.15	313.00	2040.15	INR	successful	2018-03-15	2018-03-15	13
14	2343.00	10.15	313.00	2040.15	INR	successful	2018-03-15	2018-03-15	14
\.


--
-- Name: paywithpaypal_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('paywithpaypal_payment_id_seq', 14, true);


--
-- Data for Name: paywithpaypal_paypaldetail; Type: TABLE DATA; Schema: public; Owner: root
--

COPY paywithpaypal_paypaldetail (id, payment_id, state, cart, payer_payment_method, payer_status, payer_email, payer_id, payer_country_code, transactions_amount, transactions_currency, payee_merchant_id, payee_email, description, payment_mode, reason_code, protection_eligibility, transaction_fee, created_at, updated_at, order_id_id) FROM stdin;
12	PAY-1CF6915099755661VLKURA6Y	approved	4C3234533V611571L	paypal	VERIFIED	amruta-buyer@zenrays.com	8UKSC7SP96MGA	IN	3015.00	INR	\N	\N	Pay with Paypal	\N	\N	\N	\N	2018-03-14	2018-03-14	12
13	PAY-14108400R73490510LKVAPMA	approved	9GA31760JY272394V	paypal	VERIFIED	amruta-buyer@zenrays.com	8UKSC7SP96MGA	IN	2040.15	INR	\N	\N	Pay with Paypal	\N	\N	\N	\N	2018-03-15	2018-03-15	13
14	PAY-8KR621572M5483243LKVBZNQ	approved	62935122DH960703U	paypal	VERIFIED	amruta-buyer@zenrays.com	8UKSC7SP96MGA	IN	2040.15	INR	\N	\N	Pay with Paypal	\N	\N	\N	\N	2018-03-15	2018-03-15	14
\.


--
-- Name: paywithpaypal_paypaldetail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('paywithpaypal_paypaldetail_id_seq', 14, true);


--
-- Data for Name: paywithpaypal_tax; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY paywithpaypal_tax (id, name, description, value) FROM stdin;
3	Service Tax	Service Tax in pecentage	0.50
\.


--
-- Name: paywithpaypal_tax_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('paywithpaypal_tax_id_seq', 3, true);


--
-- Data for Name: quizzes_answers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY quizzes_answers (id, answer, is_correct, status, "order", question_id_id) FROM stdin;
\.


--
-- Name: quizzes_answers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('quizzes_answers_id_seq', 1, false);


--
-- Data for Name: quizzes_questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY quizzes_questions (id, content, status, "order", quiz_id_id, type_id_id) FROM stdin;
\.


--
-- Name: quizzes_questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('quizzes_questions_id_seq', 1, false);


--
-- Data for Name: quizzes_questiontypes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY quizzes_questiontypes (id, name) FROM stdin;
\.


--
-- Name: quizzes_questiontypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('quizzes_questiontypes_id_seq', 1, false);


--
-- Data for Name: quizzes_quizprogress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY quizzes_quizprogress (id, score, score_outof, status, correct_questions, wrong_questions, skipped_questions, quiz_id_id, user_id_id) FROM stdin;
\.


--
-- Name: quizzes_quizprogress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('quizzes_quizprogress_id_seq', 1, false);


--
-- Data for Name: quizzes_quizzes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY quizzes_quizzes (id, title, description, created_at, course_section_id_id, user_id_id) FROM stdin;
\.


--
-- Name: quizzes_quizzes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('quizzes_quizzes_id_seq', 1, false);


--
-- Data for Name: social_auth_association; Type: TABLE DATA; Schema: public; Owner: root
--

COPY social_auth_association (id, server_url, handle, secret, issued, lifetime, assoc_type) FROM stdin;
\.


--
-- Name: social_auth_association_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('social_auth_association_id_seq', 1, false);


--
-- Data for Name: social_auth_code; Type: TABLE DATA; Schema: public; Owner: root
--

COPY social_auth_code (id, email, code, verified, "timestamp") FROM stdin;
\.


--
-- Name: social_auth_code_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('social_auth_code_id_seq', 1, false);


--
-- Data for Name: social_auth_nonce; Type: TABLE DATA; Schema: public; Owner: root
--

COPY social_auth_nonce (id, server_url, "timestamp", salt) FROM stdin;
\.


--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('social_auth_nonce_id_seq', 1, false);


--
-- Data for Name: social_auth_partial; Type: TABLE DATA; Schema: public; Owner: root
--

COPY social_auth_partial (id, token, next_step, backend, data, "timestamp") FROM stdin;
\.


--
-- Name: social_auth_partial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('social_auth_partial_id_seq', 1, false);


--
-- Data for Name: social_auth_usersocialauth; Type: TABLE DATA; Schema: public; Owner: root
--

COPY social_auth_usersocialauth (id, provider, uid, extra_data, user_id) FROM stdin;
\.


--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('social_auth_usersocialauth_id_seq', 1, false);


--
-- Data for Name: users_subcategoryroles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users_subcategoryroles (id, created_at, updated_at, role_type_id, subcategory_id_id, user_id_id) FROM stdin;
2	2018-04-27	2018-04-27	7	1	1
5	2018-04-28	2018-04-28	7	5	3
\.


--
-- Name: users_subcategoryroles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('users_subcategoryroles_id_seq', 5, true);


--
-- Data for Name: zenvimeo_item; Type: TABLE DATA; Schema: public; Owner: root
--

COPY zenvimeo_item (id, title, description, video, video_group_id) FROM stdin;
\.


--
-- Name: zenvimeo_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('zenvimeo_item_id_seq', 5, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: courses_category courses_category_name_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_category
    ADD CONSTRAINT courses_category_name_key UNIQUE (name);


--
-- Name: courses_category courses_category_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_category
    ADD CONSTRAINT courses_category_pkey PRIMARY KEY (id);


--
-- Name: courses_course_instructor_id courses_course_instructo_course_id_instructor_id_af31ebb6_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_course_instructor_id
    ADD CONSTRAINT courses_course_instructo_course_id_instructor_id_af31ebb6_uniq UNIQUE (course_id, instructor_id);


--
-- Name: courses_course_instructor_id courses_course_instructor_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_course_instructor_id
    ADD CONSTRAINT courses_course_instructor_id_pkey PRIMARY KEY (id);


--
-- Name: courses_course courses_course_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course
    ADD CONSTRAINT courses_course_pkey PRIMARY KEY (id);


--
-- Name: courses_course courses_course_slug_9c670f14_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course
    ADD CONSTRAINT courses_course_slug_9c670f14_uniq UNIQUE (slug);


--
-- Name: courses_course_tags courses_course_tags_course_id_tag_id_52b73814_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course_tags
    ADD CONSTRAINT courses_course_tags_course_id_tag_id_52b73814_uniq UNIQUE (course_id, tag_id);


--
-- Name: courses_course_tags courses_course_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course_tags
    ADD CONSTRAINT courses_course_tags_pkey PRIMARY KEY (id);


--
-- Name: courses_curriculumlecture courses_curriculumlecture_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_curriculumlecture
    ADD CONSTRAINT courses_curriculumlecture_pkey PRIMARY KEY (id);


--
-- Name: courses_curriculumsection courses_curriculumsection_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_curriculumsection
    ADD CONSTRAINT courses_curriculumsection_pkey PRIMARY KEY (id);


--
-- Name: courses_include courses_include_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_include
    ADD CONSTRAINT courses_include_pkey PRIMARY KEY (id);


--
-- Name: courses_instructor courses_instructor_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_instructor
    ADD CONSTRAINT courses_instructor_pkey PRIMARY KEY (id);


--
-- Name: courses_instructor courses_instructor_user_id_id_0113bea3_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_instructor
    ADD CONSTRAINT courses_instructor_user_id_id_0113bea3_uniq UNIQUE (user_id_id);


--
-- Name: courses_language courses_language_name_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_language
    ADD CONSTRAINT courses_language_name_key UNIQUE (name);


--
-- Name: courses_language courses_language_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_language
    ADD CONSTRAINT courses_language_pkey PRIMARY KEY (id);


--
-- Name: courses_studentreview courses_studentreview_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_studentreview
    ADD CONSTRAINT courses_studentreview_pkey PRIMARY KEY (id);


--
-- Name: courses_studentreviewvote courses_studentreviewvote_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_studentreviewvote
    ADD CONSTRAINT courses_studentreviewvote_pkey PRIMARY KEY (id);


--
-- Name: courses_subcategory courses_subcategory_name_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_subcategory
    ADD CONSTRAINT courses_subcategory_name_key UNIQUE (name);


--
-- Name: courses_subcategory courses_subcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_subcategory
    ADD CONSTRAINT courses_subcategory_pkey PRIMARY KEY (id);


--
-- Name: courses_tag courses_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_tag
    ADD CONSTRAINT courses_tag_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: drafts_approvedcourses drafts_approvedcourses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_approvedcourses
    ADD CONSTRAINT drafts_approvedcourses_pkey PRIMARY KEY (id);


--
-- Name: drafts_coursesroles drafts_coursesroles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_coursesroles
    ADD CONSTRAINT drafts_coursesroles_pkey PRIMARY KEY (id);


--
-- Name: drafts_curriculumlecture drafts_curriculumlecture_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_curriculumlecture
    ADD CONSTRAINT drafts_curriculumlecture_pkey PRIMARY KEY (id);


--
-- Name: drafts_curriculumsection drafts_curriculumsection_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_curriculumsection
    ADD CONSTRAINT drafts_curriculumsection_pkey PRIMARY KEY (id);


--
-- Name: drafts_draftcourse_instructor drafts_draftcourse_instr_draftcourse_id_instructo_21280a4f_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_instructor
    ADD CONSTRAINT drafts_draftcourse_instr_draftcourse_id_instructo_21280a4f_uniq UNIQUE (draftcourse_id, instructor_id);


--
-- Name: drafts_draftcourse_instructor drafts_draftcourse_instructor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_instructor
    ADD CONSTRAINT drafts_draftcourse_instructor_pkey PRIMARY KEY (id);


--
-- Name: drafts_draftcourse drafts_draftcourse_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse
    ADD CONSTRAINT drafts_draftcourse_pkey PRIMARY KEY (id);


--
-- Name: drafts_draftcourse drafts_draftcourse_slug_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse
    ADD CONSTRAINT drafts_draftcourse_slug_key UNIQUE (slug);


--
-- Name: drafts_draftcourse_tags drafts_draftcourse_tags_draftcourse_id_tag_id_eb6ea74d_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_tags
    ADD CONSTRAINT drafts_draftcourse_tags_draftcourse_id_tag_id_eb6ea74d_uniq UNIQUE (draftcourse_id, tag_id);


--
-- Name: drafts_draftcourse_tags drafts_draftcourse_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_tags
    ADD CONSTRAINT drafts_draftcourse_tags_pkey PRIMARY KEY (id);


--
-- Name: drafts_reasonsrejected drafts_reasonsrejected_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_reasonsrejected
    ADD CONSTRAINT drafts_reasonsrejected_pkey PRIMARY KEY (id);


--
-- Name: drafts_reviewedcourses drafts_reviewedcourses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_reviewedcourses
    ADD CONSTRAINT drafts_reviewedcourses_pkey PRIMARY KEY (id);


--
-- Name: guroomed_inprogress guroomed_inprogress_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_inprogress
    ADD CONSTRAINT guroomed_inprogress_pkey PRIMARY KEY (id);


--
-- Name: guroomed_notificationtypes guroomed_notificationtypes_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_notificationtypes
    ADD CONSTRAINT guroomed_notificationtypes_pkey PRIMARY KEY (id);


--
-- Name: guroomed_usercart guroomed_usercart_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY guroomed_usercart
    ADD CONSTRAINT guroomed_usercart_pkey PRIMARY KEY (id);


--
-- Name: guroomed_usercourses guroomed_usercourses_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usercourses
    ADD CONSTRAINT guroomed_usercourses_pkey PRIMARY KEY (id);


--
-- Name: guroomed_userinfo guroomed_userinfo_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userinfo
    ADD CONSTRAINT guroomed_userinfo_pkey PRIMARY KEY (id);


--
-- Name: guroomed_usernotification guroomed_usernotification_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usernotification
    ADD CONSTRAINT guroomed_usernotification_pkey PRIMARY KEY (id);


--
-- Name: guroomed_userprivacy guroomed_userprivacy_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userprivacy
    ADD CONSTRAINT guroomed_userprivacy_pkey PRIMARY KEY (id);


--
-- Name: homepage_footerstrip homepage_footerstrip_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY homepage_footerstrip
    ADD CONSTRAINT homepage_footerstrip_pkey PRIMARY KEY (id);


--
-- Name: homepage_infostrip homepage_infostrip_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY homepage_infostrip
    ADD CONSTRAINT homepage_infostrip_pkey PRIMARY KEY (id);


--
-- Name: paywithpaypal_order paywithpaypal_order_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_order
    ADD CONSTRAINT paywithpaypal_order_pkey PRIMARY KEY (id);


--
-- Name: paywithpaypal_ordercourse paywithpaypal_ordercourse_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY paywithpaypal_ordercourse
    ADD CONSTRAINT paywithpaypal_ordercourse_pkey PRIMARY KEY (id);


--
-- Name: paywithpaypal_payment paywithpaypal_payment_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_payment
    ADD CONSTRAINT paywithpaypal_payment_pkey PRIMARY KEY (id);


--
-- Name: paywithpaypal_paypaldetail paywithpaypal_paypaldetail_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_paypaldetail
    ADD CONSTRAINT paywithpaypal_paypaldetail_pkey PRIMARY KEY (id);


--
-- Name: paywithpaypal_tax paywithpaypal_tax_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY paywithpaypal_tax
    ADD CONSTRAINT paywithpaypal_tax_pkey PRIMARY KEY (id);


--
-- Name: quizzes_answers quizzes_answers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_answers
    ADD CONSTRAINT quizzes_answers_pkey PRIMARY KEY (id);


--
-- Name: quizzes_questions quizzes_questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_questions
    ADD CONSTRAINT quizzes_questions_pkey PRIMARY KEY (id);


--
-- Name: quizzes_questiontypes quizzes_questiontypes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_questiontypes
    ADD CONSTRAINT quizzes_questiontypes_pkey PRIMARY KEY (id);


--
-- Name: quizzes_quizprogress quizzes_quizprogress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizprogress
    ADD CONSTRAINT quizzes_quizprogress_pkey PRIMARY KEY (id);


--
-- Name: quizzes_quizzes quizzes_quizzes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizzes
    ADD CONSTRAINT quizzes_quizzes_pkey PRIMARY KEY (id);


--
-- Name: social_auth_association social_auth_association_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_association
    ADD CONSTRAINT social_auth_association_pkey PRIMARY KEY (id);


--
-- Name: social_auth_association social_auth_association_server_url_handle_078befa2_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_association
    ADD CONSTRAINT social_auth_association_server_url_handle_078befa2_uniq UNIQUE (server_url, handle);


--
-- Name: social_auth_code social_auth_code_email_code_801b2d02_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_code
    ADD CONSTRAINT social_auth_code_email_code_801b2d02_uniq UNIQUE (email, code);


--
-- Name: social_auth_code social_auth_code_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_code
    ADD CONSTRAINT social_auth_code_pkey PRIMARY KEY (id);


--
-- Name: social_auth_nonce social_auth_nonce_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_nonce
    ADD CONSTRAINT social_auth_nonce_pkey PRIMARY KEY (id);


--
-- Name: social_auth_nonce social_auth_nonce_server_url_timestamp_salt_f6284463_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_nonce
    ADD CONSTRAINT social_auth_nonce_server_url_timestamp_salt_f6284463_uniq UNIQUE (server_url, "timestamp", salt);


--
-- Name: social_auth_partial social_auth_partial_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_partial
    ADD CONSTRAINT social_auth_partial_pkey PRIMARY KEY (id);


--
-- Name: social_auth_usersocialauth social_auth_usersocialauth_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocialauth_pkey PRIMARY KEY (id);


--
-- Name: social_auth_usersocialauth social_auth_usersocialauth_provider_uid_e6b5e668_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocialauth_provider_uid_e6b5e668_uniq UNIQUE (provider, uid);


--
-- Name: users_subcategoryroles users_subcategoryroles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users_subcategoryroles
    ADD CONSTRAINT users_subcategoryroles_pkey PRIMARY KEY (id);


--
-- Name: zenvimeo_item zenvimeo_item_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY zenvimeo_item
    ADD CONSTRAINT zenvimeo_item_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: courses_category_name_016b219d_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_category_name_016b219d_like ON courses_category USING btree (name varchar_pattern_ops);


--
-- Name: courses_course_course_language_id_id_c1b6611b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_course_course_language_id_id_c1b6611b ON courses_course USING btree (course_language_id_id);


--
-- Name: courses_course_course_subcategory_id_id_32b816b7; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_course_course_subcategory_id_id_32b816b7 ON courses_course USING btree (course_subcategory_id_id);


--
-- Name: courses_course_instructor_id_course_id_af80b8b3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX courses_course_instructor_id_course_id_af80b8b3 ON courses_course_instructor_id USING btree (course_id);


--
-- Name: courses_course_instructor_id_instructor_id_1cc8719c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX courses_course_instructor_id_instructor_id_1cc8719c ON courses_course_instructor_id USING btree (instructor_id);


--
-- Name: courses_course_slug_9c670f14_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_course_slug_9c670f14_like ON courses_course USING btree (slug varchar_pattern_ops);


--
-- Name: courses_course_tags_course_id_f326f2c6; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_course_tags_course_id_f326f2c6 ON courses_course_tags USING btree (course_id);


--
-- Name: courses_course_tags_tag_id_20fb041b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_course_tags_tag_id_20fb041b ON courses_course_tags USING btree (tag_id);


--
-- Name: courses_curriculumlecture_curriculum_section_id_id_72c33348; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_curriculumlecture_curriculum_section_id_id_72c33348 ON courses_curriculumlecture USING btree (curriculum_section_id_id);


--
-- Name: courses_curriculumsection_course_id_id_04f029c9; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_curriculumsection_course_id_id_04f029c9 ON courses_curriculumsection USING btree (course_id_id);


--
-- Name: courses_include_course_id_id_6cea0d72; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_include_course_id_id_6cea0d72 ON courses_include USING btree (course_id_id);


--
-- Name: courses_language_name_30c6fb47_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_language_name_30c6fb47_like ON courses_language USING btree (name varchar_pattern_ops);


--
-- Name: courses_studentreview_course_id_id_8462eea2; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_studentreview_course_id_id_8462eea2 ON courses_studentreview USING btree (course_id_id);


--
-- Name: courses_studentreview_user_id_id_36825971; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_studentreview_user_id_id_36825971 ON courses_studentreview USING btree (user_id_id);


--
-- Name: courses_studentreviewvote_review_id_id_bb675b60; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX courses_studentreviewvote_review_id_id_bb675b60 ON courses_studentreviewvote USING btree (review_id_id);


--
-- Name: courses_studentreviewvote_user_id_id_b4981937; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX courses_studentreviewvote_user_id_id_b4981937 ON courses_studentreviewvote USING btree (user_id_id);


--
-- Name: courses_subcategory_course_category_id_id_1a02a90a; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_subcategory_course_category_id_id_1a02a90a ON courses_subcategory USING btree (course_category_id_id);


--
-- Name: courses_subcategory_name_1aa0f045_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX courses_subcategory_name_1aa0f045_like ON courses_subcategory USING btree (name varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: drafts_approvedcourses_course_draft_id_id_7511d1c9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_approvedcourses_course_draft_id_id_7511d1c9 ON drafts_approvedcourses USING btree (course_draft_id_id);


--
-- Name: drafts_approvedcourses_reason_rejected_id_43992f56; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_approvedcourses_reason_rejected_id_43992f56 ON drafts_approvedcourses USING btree (reason_rejected_id);


--
-- Name: drafts_approvedcourses_user_id_id_f293cd63; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_approvedcourses_user_id_id_f293cd63 ON drafts_approvedcourses USING btree (user_id_id);


--
-- Name: drafts_coursesroles_draft_course_id_id_bb293b72; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_coursesroles_draft_course_id_id_bb293b72 ON drafts_coursesroles USING btree (course_draft_id_id);


--
-- Name: drafts_coursesroles_role_type_id_80a67cea; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_coursesroles_role_type_id_80a67cea ON drafts_coursesroles USING btree (role_type_id);


--
-- Name: drafts_coursesroles_user_id_id_80b38b92; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_coursesroles_user_id_id_80b38b92 ON drafts_coursesroles USING btree (user_id_id);


--
-- Name: drafts_curriculumlecture_curriculum_section_id_id_2c587bd7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_curriculumlecture_curriculum_section_id_id_2c587bd7 ON drafts_curriculumlecture USING btree (curriculum_section_id_id);


--
-- Name: drafts_curriculumsection_course_draft_id_id_38fd6ed0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_curriculumsection_course_draft_id_id_38fd6ed0 ON drafts_curriculumsection USING btree (course_draft_id_id);


--
-- Name: drafts_draftcourse_course_language_id_dfd7b397; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_draftcourse_course_language_id_dfd7b397 ON drafts_draftcourse USING btree (course_language_id);


--
-- Name: drafts_draftcourse_course_subcategory_id_59d9d41b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_draftcourse_course_subcategory_id_59d9d41b ON drafts_draftcourse USING btree (course_subcategory_id);


--
-- Name: drafts_draftcourse_instructor_draftcourse_id_4fa4d5c9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_draftcourse_instructor_draftcourse_id_4fa4d5c9 ON drafts_draftcourse_instructor USING btree (draftcourse_id);


--
-- Name: drafts_draftcourse_instructor_instructor_id_2e1e1bd8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_draftcourse_instructor_instructor_id_2e1e1bd8 ON drafts_draftcourse_instructor USING btree (instructor_id);


--
-- Name: drafts_draftcourse_slug_2beded11_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_draftcourse_slug_2beded11_like ON drafts_draftcourse USING btree (slug varchar_pattern_ops);


--
-- Name: drafts_draftcourse_tags_draftcourse_id_b4fb6ae3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_draftcourse_tags_draftcourse_id_b4fb6ae3 ON drafts_draftcourse_tags USING btree (draftcourse_id);


--
-- Name: drafts_draftcourse_tags_tag_id_214fb4ab; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_draftcourse_tags_tag_id_214fb4ab ON drafts_draftcourse_tags USING btree (tag_id);


--
-- Name: drafts_reviewedcourses_course_draft_id_id_4ab98f05; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_reviewedcourses_course_draft_id_id_4ab98f05 ON drafts_reviewedcourses USING btree (course_draft_id_id);


--
-- Name: drafts_reviewedcourses_reason_rejected_id_276d1e5d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_reviewedcourses_reason_rejected_id_276d1e5d ON drafts_reviewedcourses USING btree (reason_rejected_id);


--
-- Name: drafts_reviewedcourses_user_id_id_01036c88; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX drafts_reviewedcourses_user_id_id_01036c88 ON drafts_reviewedcourses USING btree (user_id_id);


--
-- Name: guroomed_inprogress_courses_lecture_id_id_b8a46fd2; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_inprogress_courses_lecture_id_id_b8a46fd2 ON guroomed_inprogress USING btree (courses_lecture_id_id);


--
-- Name: guroomed_usercart_course_id_id_ba4d01c4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX guroomed_usercart_course_id_id_ba4d01c4 ON guroomed_usercart USING btree (course_id_id);


--
-- Name: guroomed_usercart_user_id_id_65b4d0ea; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX guroomed_usercart_user_id_id_65b4d0ea ON guroomed_usercart USING btree (user_id_id);


--
-- Name: guroomed_usercourses_course_id_id_ab49b250; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_usercourses_course_id_id_ab49b250 ON guroomed_usercourses USING btree (course_id_id);


--
-- Name: guroomed_usercourses_in_progress_id_6133ed85; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_usercourses_in_progress_id_6133ed85 ON guroomed_usercourses USING btree (in_progress_id);


--
-- Name: guroomed_usercourses_user_id_id_b0890643; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_usercourses_user_id_id_b0890643 ON guroomed_usercourses USING btree (user_id_id);


--
-- Name: guroomed_userinfo_created_by_id_c1e68cba; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_userinfo_created_by_id_c1e68cba ON guroomed_userinfo USING btree (created_by_id);


--
-- Name: guroomed_userinfo_language_id_e76ba924; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_userinfo_language_id_e76ba924 ON guroomed_userinfo USING btree (language_id);


--
-- Name: guroomed_userinfo_user_id_id_5ccdd4f0; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_userinfo_user_id_id_5ccdd4f0 ON guroomed_userinfo USING btree (user_id_id);


--
-- Name: guroomed_usernotification_notification_id_id_8df354e3; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_usernotification_notification_id_id_8df354e3 ON guroomed_usernotification USING btree (notification_id_id);


--
-- Name: guroomed_usernotification_user_id_id_6a14f360; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_usernotification_user_id_id_6a14f360 ON guroomed_usernotification USING btree (user_id_id);


--
-- Name: guroomed_userprivacy_user_id_id_315a12cc; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX guroomed_userprivacy_user_id_id_315a12cc ON guroomed_userprivacy USING btree (user_id_id);


--
-- Name: paywithpaypal_order_user_id_id_48055ccf; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX paywithpaypal_order_user_id_id_48055ccf ON paywithpaypal_order USING btree (user_id_id);


--
-- Name: paywithpaypal_ordercourse_course_id_id_735645f5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX paywithpaypal_ordercourse_course_id_id_735645f5 ON paywithpaypal_ordercourse USING btree (course_id_id);


--
-- Name: paywithpaypal_ordercourse_order_id_id_9304e6fb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX paywithpaypal_ordercourse_order_id_id_9304e6fb ON paywithpaypal_ordercourse USING btree (order_id_id);


--
-- Name: paywithpaypal_payment_order_id_id_ed4db6ee; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX paywithpaypal_payment_order_id_id_ed4db6ee ON paywithpaypal_payment USING btree (order_id_id);


--
-- Name: paywithpaypal_paypaldetail_order_id_id_a8f1f22a; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX paywithpaypal_paypaldetail_order_id_id_a8f1f22a ON paywithpaypal_paypaldetail USING btree (order_id_id);


--
-- Name: quizzes_answers_question_id_id_315b43ac; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX quizzes_answers_question_id_id_315b43ac ON quizzes_answers USING btree (question_id_id);


--
-- Name: quizzes_questions_quiz_id_id_388617b6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX quizzes_questions_quiz_id_id_388617b6 ON quizzes_questions USING btree (quiz_id_id);


--
-- Name: quizzes_questions_type_id_id_e680e1d8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX quizzes_questions_type_id_id_e680e1d8 ON quizzes_questions USING btree (type_id_id);


--
-- Name: quizzes_quizprogress_quiz_id_id_1ae778ed; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX quizzes_quizprogress_quiz_id_id_1ae778ed ON quizzes_quizprogress USING btree (quiz_id_id);


--
-- Name: quizzes_quizprogress_user_id_id_6b62df1c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX quizzes_quizprogress_user_id_id_6b62df1c ON quizzes_quizprogress USING btree (user_id_id);


--
-- Name: quizzes_quizzes_course_section_id_id_3f595843; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX quizzes_quizzes_course_section_id_id_3f595843 ON quizzes_quizzes USING btree (course_section_id_id);


--
-- Name: quizzes_quizzes_user_id_id_1a36504d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX quizzes_quizzes_user_id_id_1a36504d ON quizzes_quizzes USING btree (user_id_id);


--
-- Name: social_auth_code_code_a2393167; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX social_auth_code_code_a2393167 ON social_auth_code USING btree (code);


--
-- Name: social_auth_code_code_a2393167_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX social_auth_code_code_a2393167_like ON social_auth_code USING btree (code varchar_pattern_ops);


--
-- Name: social_auth_code_timestamp_176b341f; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX social_auth_code_timestamp_176b341f ON social_auth_code USING btree ("timestamp");


--
-- Name: social_auth_partial_timestamp_50f2119f; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX social_auth_partial_timestamp_50f2119f ON social_auth_partial USING btree ("timestamp");


--
-- Name: social_auth_partial_token_3017fea3; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX social_auth_partial_token_3017fea3 ON social_auth_partial USING btree (token);


--
-- Name: social_auth_partial_token_3017fea3_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX social_auth_partial_token_3017fea3_like ON social_auth_partial USING btree (token varchar_pattern_ops);


--
-- Name: social_auth_usersocialauth_user_id_17d28448; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX social_auth_usersocialauth_user_id_17d28448 ON social_auth_usersocialauth USING btree (user_id);


--
-- Name: users_subcategoryroles_role_type_id_f3fb2a0c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_subcategoryroles_role_type_id_f3fb2a0c ON users_subcategoryroles USING btree (role_type_id);


--
-- Name: users_subcategoryroles_subcategory_id_id_c11a11a8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_subcategoryroles_subcategory_id_id_c11a11a8 ON users_subcategoryroles USING btree (subcategory_id_id);


--
-- Name: users_subcategoryroles_user_id_id_efb2139b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_subcategoryroles_user_id_id_efb2139b ON users_subcategoryroles USING btree (user_id_id);


--
-- Name: zenvimeo_item_video_group_id_d5f1dc52; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX zenvimeo_item_video_group_id_d5f1dc52 ON zenvimeo_item USING btree (video_group_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_course courses_course_course_language_id_i_c1b6611b_fk_courses_l; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course
    ADD CONSTRAINT courses_course_course_language_id_i_c1b6611b_fk_courses_l FOREIGN KEY (course_language_id_id) REFERENCES courses_language(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_course courses_course_course_subcategory_i_32b816b7_fk_courses_s; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course
    ADD CONSTRAINT courses_course_course_subcategory_i_32b816b7_fk_courses_s FOREIGN KEY (course_subcategory_id_id) REFERENCES courses_subcategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_course_instructor_id courses_course_instr_course_id_af80b8b3_fk_courses_c; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_course_instructor_id
    ADD CONSTRAINT courses_course_instr_course_id_af80b8b3_fk_courses_c FOREIGN KEY (course_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_course_instructor_id courses_course_instr_instructor_id_1cc8719c_fk_courses_i; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_course_instructor_id
    ADD CONSTRAINT courses_course_instr_instructor_id_1cc8719c_fk_courses_i FOREIGN KEY (instructor_id) REFERENCES courses_instructor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_course_tags courses_course_tags_course_id_f326f2c6_fk_courses_course_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course_tags
    ADD CONSTRAINT courses_course_tags_course_id_f326f2c6_fk_courses_course_id FOREIGN KEY (course_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_course_tags courses_course_tags_tag_id_20fb041b_fk_courses_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_course_tags
    ADD CONSTRAINT courses_course_tags_tag_id_20fb041b_fk_courses_tag_id FOREIGN KEY (tag_id) REFERENCES courses_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_curriculumlecture courses_curriculumle_curriculum_section_i_72c33348_fk_courses_c; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_curriculumlecture
    ADD CONSTRAINT courses_curriculumle_curriculum_section_i_72c33348_fk_courses_c FOREIGN KEY (curriculum_section_id_id) REFERENCES courses_curriculumsection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_curriculumsection courses_curriculumse_course_id_id_04f029c9_fk_courses_c; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_curriculumsection
    ADD CONSTRAINT courses_curriculumse_course_id_id_04f029c9_fk_courses_c FOREIGN KEY (course_id_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_include courses_include_course_id_id_6cea0d72_fk_courses_course_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_include
    ADD CONSTRAINT courses_include_course_id_id_6cea0d72_fk_courses_course_id FOREIGN KEY (course_id_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_instructor courses_instructor_user_id_id_0113bea3_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_instructor
    ADD CONSTRAINT courses_instructor_user_id_id_0113bea3_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_studentreview courses_studentrevie_course_id_id_8462eea2_fk_courses_c; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_studentreview
    ADD CONSTRAINT courses_studentrevie_course_id_id_8462eea2_fk_courses_c FOREIGN KEY (course_id_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_studentreviewvote courses_studentrevie_review_id_id_bb675b60_fk_courses_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_studentreviewvote
    ADD CONSTRAINT courses_studentrevie_review_id_id_bb675b60_fk_courses_s FOREIGN KEY (review_id_id) REFERENCES courses_studentreview(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_studentreview courses_studentreview_user_id_id_36825971_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_studentreview
    ADD CONSTRAINT courses_studentreview_user_id_id_36825971_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_studentreviewvote courses_studentreviewvote_user_id_id_b4981937_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY courses_studentreviewvote
    ADD CONSTRAINT courses_studentreviewvote_user_id_id_b4981937_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_subcategory courses_subcategory_course_category_id_i_1a02a90a_fk_courses_c; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY courses_subcategory
    ADD CONSTRAINT courses_subcategory_course_category_id_i_1a02a90a_fk_courses_c FOREIGN KEY (course_category_id_id) REFERENCES courses_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_approvedcourses drafts_approvedcours_course_draft_id_id_7511d1c9_fk_drafts_dr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_approvedcourses
    ADD CONSTRAINT drafts_approvedcours_course_draft_id_id_7511d1c9_fk_drafts_dr FOREIGN KEY (course_draft_id_id) REFERENCES drafts_draftcourse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_approvedcourses drafts_approvedcours_reason_rejected_id_43992f56_fk_drafts_re; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_approvedcourses
    ADD CONSTRAINT drafts_approvedcours_reason_rejected_id_43992f56_fk_drafts_re FOREIGN KEY (reason_rejected_id) REFERENCES drafts_reasonsrejected(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_approvedcourses drafts_approvedcourses_user_id_id_f293cd63_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_approvedcourses
    ADD CONSTRAINT drafts_approvedcourses_user_id_id_f293cd63_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_coursesroles drafts_coursesroles_course_draft_id_id_44d94385_fk_drafts_dr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_coursesroles
    ADD CONSTRAINT drafts_coursesroles_course_draft_id_id_44d94385_fk_drafts_dr FOREIGN KEY (course_draft_id_id) REFERENCES drafts_draftcourse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_coursesroles drafts_coursesroles_role_type_id_80a67cea_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_coursesroles
    ADD CONSTRAINT drafts_coursesroles_role_type_id_80a67cea_fk_auth_group_id FOREIGN KEY (role_type_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_coursesroles drafts_coursesroles_user_id_id_80b38b92_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_coursesroles
    ADD CONSTRAINT drafts_coursesroles_user_id_id_80b38b92_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_curriculumlecture drafts_curriculumlec_curriculum_section_i_2c587bd7_fk_drafts_cu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_curriculumlecture
    ADD CONSTRAINT drafts_curriculumlec_curriculum_section_i_2c587bd7_fk_drafts_cu FOREIGN KEY (curriculum_section_id_id) REFERENCES drafts_curriculumsection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_curriculumsection drafts_curriculumsec_course_draft_id_id_38fd6ed0_fk_drafts_dr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_curriculumsection
    ADD CONSTRAINT drafts_curriculumsec_course_draft_id_id_38fd6ed0_fk_drafts_dr FOREIGN KEY (course_draft_id_id) REFERENCES drafts_draftcourse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_draftcourse drafts_draftcourse_course_language_id_dfd7b397_fk_courses_l; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse
    ADD CONSTRAINT drafts_draftcourse_course_language_id_dfd7b397_fk_courses_l FOREIGN KEY (course_language_id) REFERENCES courses_language(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_draftcourse drafts_draftcourse_course_subcategory_i_59d9d41b_fk_courses_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse
    ADD CONSTRAINT drafts_draftcourse_course_subcategory_i_59d9d41b_fk_courses_s FOREIGN KEY (course_subcategory_id) REFERENCES courses_subcategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_draftcourse_instructor drafts_draftcourse_i_draftcourse_id_4fa4d5c9_fk_drafts_dr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_instructor
    ADD CONSTRAINT drafts_draftcourse_i_draftcourse_id_4fa4d5c9_fk_drafts_dr FOREIGN KEY (draftcourse_id) REFERENCES drafts_draftcourse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_draftcourse_instructor drafts_draftcourse_i_instructor_id_2e1e1bd8_fk_courses_i; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_instructor
    ADD CONSTRAINT drafts_draftcourse_i_instructor_id_2e1e1bd8_fk_courses_i FOREIGN KEY (instructor_id) REFERENCES courses_instructor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_draftcourse_tags drafts_draftcourse_t_draftcourse_id_b4fb6ae3_fk_drafts_dr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_tags
    ADD CONSTRAINT drafts_draftcourse_t_draftcourse_id_b4fb6ae3_fk_drafts_dr FOREIGN KEY (draftcourse_id) REFERENCES drafts_draftcourse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_draftcourse_tags drafts_draftcourse_tags_tag_id_214fb4ab_fk_courses_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_draftcourse_tags
    ADD CONSTRAINT drafts_draftcourse_tags_tag_id_214fb4ab_fk_courses_tag_id FOREIGN KEY (tag_id) REFERENCES courses_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_reviewedcourses drafts_reviewedcours_course_draft_id_id_4ab98f05_fk_drafts_dr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_reviewedcourses
    ADD CONSTRAINT drafts_reviewedcours_course_draft_id_id_4ab98f05_fk_drafts_dr FOREIGN KEY (course_draft_id_id) REFERENCES drafts_draftcourse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_reviewedcourses drafts_reviewedcours_reason_rejected_id_276d1e5d_fk_drafts_re; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_reviewedcourses
    ADD CONSTRAINT drafts_reviewedcours_reason_rejected_id_276d1e5d_fk_drafts_re FOREIGN KEY (reason_rejected_id) REFERENCES drafts_reasonsrejected(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drafts_reviewedcourses drafts_reviewedcourses_user_id_id_01036c88_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY drafts_reviewedcourses
    ADD CONSTRAINT drafts_reviewedcourses_user_id_id_01036c88_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_inprogress guroomed_inprogress_courses_lecture_id_i_b8a46fd2_fk_courses_c; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_inprogress
    ADD CONSTRAINT guroomed_inprogress_courses_lecture_id_i_b8a46fd2_fk_courses_c FOREIGN KEY (courses_lecture_id_id) REFERENCES courses_curriculumlecture(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_usercart guroomed_usercart_course_id_id_ba4d01c4_fk_courses_course_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY guroomed_usercart
    ADD CONSTRAINT guroomed_usercart_course_id_id_ba4d01c4_fk_courses_course_id FOREIGN KEY (course_id_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_usercart guroomed_usercart_user_id_id_65b4d0ea_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY guroomed_usercart
    ADD CONSTRAINT guroomed_usercart_user_id_id_65b4d0ea_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_usercourses guroomed_usercourses_course_id_id_ab49b250_fk_courses_course_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usercourses
    ADD CONSTRAINT guroomed_usercourses_course_id_id_ab49b250_fk_courses_course_id FOREIGN KEY (course_id_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_usercourses guroomed_usercourses_in_progress_id_6133ed85_fk_guroomed_; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usercourses
    ADD CONSTRAINT guroomed_usercourses_in_progress_id_6133ed85_fk_guroomed_ FOREIGN KEY (in_progress_id) REFERENCES guroomed_inprogress(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_usercourses guroomed_usercourses_user_id_id_b0890643_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usercourses
    ADD CONSTRAINT guroomed_usercourses_user_id_id_b0890643_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_userinfo guroomed_userinfo_created_by_id_c1e68cba_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userinfo
    ADD CONSTRAINT guroomed_userinfo_created_by_id_c1e68cba_fk_auth_user_id FOREIGN KEY (created_by_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_userinfo guroomed_userinfo_language_id_e76ba924_fk_courses_language_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userinfo
    ADD CONSTRAINT guroomed_userinfo_language_id_e76ba924_fk_courses_language_id FOREIGN KEY (language_id) REFERENCES courses_language(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_userinfo guroomed_userinfo_user_id_id_5ccdd4f0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userinfo
    ADD CONSTRAINT guroomed_userinfo_user_id_id_5ccdd4f0_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_usernotification guroomed_usernotific_notification_id_id_8df354e3_fk_guroomed_; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usernotification
    ADD CONSTRAINT guroomed_usernotific_notification_id_id_8df354e3_fk_guroomed_ FOREIGN KEY (notification_id_id) REFERENCES guroomed_notificationtypes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_usernotification guroomed_usernotification_user_id_id_6a14f360_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_usernotification
    ADD CONSTRAINT guroomed_usernotification_user_id_id_6a14f360_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: guroomed_userprivacy guroomed_userprivacy_user_id_id_315a12cc_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY guroomed_userprivacy
    ADD CONSTRAINT guroomed_userprivacy_user_id_id_315a12cc_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: paywithpaypal_order paywithpaypal_order_user_id_id_48055ccf_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_order
    ADD CONSTRAINT paywithpaypal_order_user_id_id_48055ccf_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: paywithpaypal_ordercourse paywithpaypal_orderc_course_id_id_735645f5_fk_courses_c; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY paywithpaypal_ordercourse
    ADD CONSTRAINT paywithpaypal_orderc_course_id_id_735645f5_fk_courses_c FOREIGN KEY (course_id_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: paywithpaypal_ordercourse paywithpaypal_orderc_order_id_id_9304e6fb_fk_paywithpa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY paywithpaypal_ordercourse
    ADD CONSTRAINT paywithpaypal_orderc_order_id_id_9304e6fb_fk_paywithpa FOREIGN KEY (order_id_id) REFERENCES paywithpaypal_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: paywithpaypal_payment paywithpaypal_paymen_order_id_id_ed4db6ee_fk_paywithpa; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_payment
    ADD CONSTRAINT paywithpaypal_paymen_order_id_id_ed4db6ee_fk_paywithpa FOREIGN KEY (order_id_id) REFERENCES paywithpaypal_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: paywithpaypal_paypaldetail paywithpaypal_paypal_order_id_id_a8f1f22a_fk_paywithpa; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY paywithpaypal_paypaldetail
    ADD CONSTRAINT paywithpaypal_paypal_order_id_id_a8f1f22a_fk_paywithpa FOREIGN KEY (order_id_id) REFERENCES paywithpaypal_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: quizzes_answers quizzes_answers_question_id_id_315b43ac_fk_quizzes_questions_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_answers
    ADD CONSTRAINT quizzes_answers_question_id_id_315b43ac_fk_quizzes_questions_id FOREIGN KEY (question_id_id) REFERENCES quizzes_questions(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: quizzes_questions quizzes_questions_quiz_id_id_388617b6_fk_quizzes_quizzes_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_questions
    ADD CONSTRAINT quizzes_questions_quiz_id_id_388617b6_fk_quizzes_quizzes_id FOREIGN KEY (quiz_id_id) REFERENCES quizzes_quizzes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: quizzes_questions quizzes_questions_type_id_id_e680e1d8_fk_quizzes_q; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_questions
    ADD CONSTRAINT quizzes_questions_type_id_id_e680e1d8_fk_quizzes_q FOREIGN KEY (type_id_id) REFERENCES quizzes_questiontypes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: quizzes_quizprogress quizzes_quizprogress_quiz_id_id_1ae778ed_fk_quizzes_quizzes_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizprogress
    ADD CONSTRAINT quizzes_quizprogress_quiz_id_id_1ae778ed_fk_quizzes_quizzes_id FOREIGN KEY (quiz_id_id) REFERENCES quizzes_quizzes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: quizzes_quizprogress quizzes_quizprogress_user_id_id_6b62df1c_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizprogress
    ADD CONSTRAINT quizzes_quizprogress_user_id_id_6b62df1c_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: quizzes_quizzes quizzes_quizzes_course_section_id_id_3f595843_fk_drafts_cu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizzes
    ADD CONSTRAINT quizzes_quizzes_course_section_id_id_3f595843_fk_drafts_cu FOREIGN KEY (course_section_id_id) REFERENCES drafts_curriculumsection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: quizzes_quizzes quizzes_quizzes_user_id_id_1a36504d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY quizzes_quizzes
    ADD CONSTRAINT quizzes_quizzes_user_id_id_1a36504d_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: social_auth_usersocialauth social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_subcategoryroles users_subcategoryrol_subcategory_id_id_c11a11a8_fk_courses_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users_subcategoryroles
    ADD CONSTRAINT users_subcategoryrol_subcategory_id_id_c11a11a8_fk_courses_s FOREIGN KEY (subcategory_id_id) REFERENCES courses_subcategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_subcategoryroles users_subcategoryroles_role_type_id_f3fb2a0c_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users_subcategoryroles
    ADD CONSTRAINT users_subcategoryroles_role_type_id_f3fb2a0c_fk_auth_group_id FOREIGN KEY (role_type_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_subcategoryroles users_subcategoryroles_user_id_id_efb2139b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users_subcategoryroles
    ADD CONSTRAINT users_subcategoryroles_user_id_id_efb2139b_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: zenvimeo_item zenvimeo_item_video_group_id_d5f1dc52_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY zenvimeo_item
    ADD CONSTRAINT zenvimeo_item_video_group_id_d5f1dc52_fk_auth_group_id FOREIGN KEY (video_group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

