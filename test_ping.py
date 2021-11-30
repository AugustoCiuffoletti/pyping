import pyping

try:
  r = pyping.ping("www.google.com", count = 1)
  print 'Dest '+str(r.destination)
  print 'max RTT '+str(r.max_rtt)
  print 'avg RTT '+str(r.avg_rtt)
  print 'min RTT '+str(r.min_rtt)
  print 'IP Dest '+str(r.destination_ip)
except Exception, e:
  print str(e)
    
