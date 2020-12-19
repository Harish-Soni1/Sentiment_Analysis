from flask import Flask, render_template, request, url_for
import jsonify
import requests
import pickle
import pandas as pd
import numpy as np
import sklearn
import os
from sklearn.preprocessing import StandardScaler



