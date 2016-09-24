#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for grit project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%5wxfnksebk2eou(wdi&czg#_vn#q8or*bwudv&4#^84u#&pmw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'exile_ui',
    'cuser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grit',
    'empresa',
    'empresa.riesgo',
    'norma',
    'norma.formulario',
    'notificacion',
    'usr',
    'validable',
    'epc',
]

EXILE_UI = {
    'site_title': 'Grit',
    'site_header': 'Grit',
    'index_title': 'Proyect planning',
    'media': {
        'logo': {
            'dashboard': '/media/grit_logo/logo-grit.png',
            'page': '/media/grit_logo/logo-grit_200.png',
            'login': '/media/grit_logo/logo-grit.png'
        },
        'icons': {
            'formulario': {
                'icon': 'content_paste',
                'groups': [
                    'Variables',
                    'Configuración'
                ],
                'models': {
                    'Tipo': {'icon': 'settings', 'group': 'Configuración'},
                    'Formulario': {'icon': 'assignment', 'group': 'Variables'},
                    'Campo': {'icon': 'input', 'group': 'Variables'},
                    'Registro': {'icon': 'insert_comment', 'group': 'Variables'},
                    'Valor': {'icon': 'settings', 'group': 'Variables'},
                    'Entrada': {'icon': 'assignment_returned', 'group': 'Variables'}
                }
            },
            'empresa': {
                'icon': 'business',
                'groups': [
                    'Empresa'
                ],
                'models': {
                    'Configuracion': {'icon': 'settings', 'group': 'Empresa'},
                    'Calculos': {'icon': 'functions', 'group': 'Empresa'},
                    'Anio': {'icon': 'date_range', 'group': 'Empresa'},
                    'Empresa': {'icon': 'business', 'group': 'Empresa'},
                    'Departamento': {'icon': 'view_compact', 'group': 'Empresa'},
                    'Cargo': {'icon': 'assignment_ind', 'group': 'Empresa'},
                    'Requisito': {'icon': 'playlist_add_check', 'group': 'Empresa'},
                    'Empleado': {'icon': 'face', 'group': 'Empresa'},
                    'Jefes': {'icon': 'supervisor_account', 'group': 'Empresa'},
                    'Contrato': {'icon': 'library_books', 'group': 'Empresa'},
                    'Asistencia': {'icon': 'spellcheck', 'group': 'Empresa'},
                    'HorasExtra': {'icon': 'alarm_add', 'group': 'Empresa'},
                    'LiquidacionNomina': {'icon': 'attach_money', 'group': 'Empresa'},
                },
            }, 'riesgo': {
                'icon': 'warning',
                'groups': [
                    'Riesgo'
                ],
                'models': {
                    'Criticidad': {'icon': 'whatshot', 'group': 'Riesgo'},
                    'ElementoProteger': {'icon': 'security', 'group': 'Riesgo'},
                    'CargoRiesgo': {'icon': 'assignment_late', 'group': 'Riesgo'},
                    'Riesgo': {'icon': 'warning', 'group': 'Riesgo'},
                    'EvaluacionEmpresa': {'icon': 'account_balance', 'group': 'Riesgo'},
                    'EvaluacionRiesgos': {'icon': 'assignment_turned_in', 'group': 'Riesgo'},
                },
            }, 'norma': {
                'icon': 'assignment',
                'groups': [
                    'Norma'
                ],
                'models': {
                    'Norma': {'icon':'assignment', 'group': 'Norma'},
                    'Item': {'icon':'list', 'group': 'Norma'},
                    'Formato': {'icon':'receipt', 'group': 'Norma'}
                }
            }, 'epc': {
                'icon': 'folder_open',
                'groups': [
                    'EPC'
                ],
                'models': {
                    'Contrato': {'group': 'EPC', 'icon': 'library_books'},
                    'Contratista': {'group': 'EPC', 'icon': 'person'},
                    'Material': {'group': 'EPC', 'icon': 'layers'},
                    'OrdenTrabajo': {'group': 'EPC', 'icon': 'near_me'},
                    'Actividad': {'group': 'EPC', 'icon': 'access_time'},
                    'Proyecto': {'group': 'EPC', 'icon': 'folder_open'},
                    'TipoAdquisiscion': {'group': 'EPC', 'icon': 'toys'},
                }
            },
            'auth': {
                'icon': 'security',
                'groups': [
                    'Seguridad',
                ],
                'models': {
                    'Group': {'icon': 'people', 'group': 'Seguridad'},
                    'User': {'icon': 'person', 'group': 'Seguridad'}
                }
            },
            'logout': {
                'icon': 'exit_to_app',
            }
        }
    }
}

MENU_ORDER = [
    {
        'name': 'formulario',
        'models': [
            'Tipo',
            'Formulario',
            'Campo',
            'Registro',
            'Valor',
            'Entrada',
        ]
    },
    {
        'name': 'empresa',
        'models': [
            'Configuracion',
            'Calculos',
            'Anio',
            'Empresa',
            'Departamento',
            'Cargo',
            'Requisito',
            'Empleado',
            'Jefes',
            'Contrato',
            'Asistencia',
            'HorasExtra',
            'LiquidacionNomina',
        ]
    }, {
        'name': 'riesgo',
        'models': [
            'Criticidad',
            'ElementoProteger',
            'CargoRiesgo',
            'Riesgo',
            'EvaluacionRiesgos',
            'EvaluacionEmpresa',
        ]
    },
    {
        'name': 'norma',
        'models': [
            'Norma',
            'Item',
            'Formato'
        ]
    },
    {
        'name': 'epc',
        'models': [
            'Contratista',
            'Material',
            'OrdenTrabajo',
            'Actividad',
            'Proyecto',
        ]
    },
    {
        'name': 'logout'
    }
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'grit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'grit',
        'USER': 'postgres',
        'PASSWORD': 'Exile*74522547',
        'HOST': '104.236.33.228',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
