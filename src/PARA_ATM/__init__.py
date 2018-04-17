'''

NASA NextGen NAS ULI Information Fusion
        
@organization: PARA Lab, Arizona State University
@author: Hari Iyer
@date: 01/19/2018

This module imports libraries and resources used in the system. The documentation on GitHub has instructions on setting these up locally.

'''


#------------------------Built-in System Modules------------------------#

import os
import re
import sys
import datetime
import urllib
import csv
import imp
import json
import importlib
import math
import glob
import time
import socket
from pathlib import Path
import xml.etree.ElementTree as ET
from ast import literal_eval

#------------------------Installed Third-Party Libraries------------------------#

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView
import matplotlib.pyplot as plt
import numpy as np
import psycopg2
import rdflib

#------------------------Application Modules------------------------#

from PARA_ATM.Commands import Airport,NATS_GateToGateSim,Helpers,PlotGraph,RegressionCurve
from PARA_ATM.Commands.Helpers import DataStore
from PARA_ATM.Map import MapView
from PARA_ATM.Ontology import QueryOntology

from NATS.Server import *