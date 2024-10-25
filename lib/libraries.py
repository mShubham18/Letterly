from src.Letterly.exceptions import CustomException
from src.Letterly import logger
import sys
import streamlit as st
import google.generativeai as genai
import os
#from openai import openai
import requests
import json
import time
from src.Letterly.components.degrees import Degree
from src.Letterly.components.skillset import Skillset
from src.Letterly.components.job_roles import Job_roles
from src.Letterly.constants.constants import notice_period,prof_journey,personal_projects