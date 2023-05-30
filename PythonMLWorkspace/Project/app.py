import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = '60253fee74455f6316932b26820c3aad'