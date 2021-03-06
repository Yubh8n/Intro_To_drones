#!/usr/bin/python
#/****************************************************************************
# nmea read function
# Copyright (c) 2018, Kjeld Jensen <kj@kjen.dk>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#****************************************************************************/
'''
2018-03-13 Kjeld First version, that reads in CSV data
'''
import numpy as np
import matplotlib.pyplot as plt
import exportkml
import utm

class nmea_class:
  def __init__(self):
    self.data = []

  def import_file(self, file_name):
    file_ok = True
    try:
      # read all lines from the file and strip \n
      lines = [line.rstrip() for line in open(file_name)] 
    except:
      file_ok = False
    if file_ok == True:
      pt_num = 0
      for i in range(len(lines)): # for all lines
        if len(lines[i]) > 0 and lines[i][0] != '#': # if not a comment or empty line
          csv = lines[i].split (',') # split into comma separated list
          self.data.append(csv)

  def print_data(self):
    for i in range(len(self.data)):
      print self.data[i]


if __name__ == "__main__":
  print 'Importing file'
  nmea = nmea_class()
  nmea.import_file ('nmea_trimble_gnss_eduquad_flight.txt')
  #nmea.print_data()




  time = []
  height = []
  Latitude = []
  Longtitude = []
  for i in range(0, np.size(nmea.data)-1):
    #if nmea.data[i][0] == "$GPGLL" and (nmea.data[i][1] != '' and nmea.data[i][3] != ''):
    Latitude.append(float(nmea.data[i][2]))
    Longtitude.append(float(nmea.data[i][4]))

  #print Latitude
  #print Longtitude

  #print time
  #print height
  kml = exportkml.kmlclass()


  kml.begin('Maps_file.kml', 'x,y', 'use of kml', 0.1)
  kml.trksegbegin ('', '', 'red', 'absolute')
  for i in range (0, np.size(Latitude)-1 ):
    Latitude[i] = int(Latitude[i])/100 + (float(Latitude[i])-(int(Latitude[i])/100)*100)/60
    Longtitude[i] = int(Longtitude[i])/100 + (float(Longtitude[i])-(int(Longtitude[i])/100)*100)/60
    #print Latitude[i], + Longtitude[i]
    kml.trkpt(float(Latitude[i]), float(Longtitude[i]), 0.0)
  kml.trksegend()
  kml.end()
  #plt.plot(time, height)
  #plt.show()
