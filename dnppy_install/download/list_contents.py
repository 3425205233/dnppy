"""
lists the contents of either an ftp or http download site and returns filenames/paths
"""

import ftplib, urllib, os, time, sys


def ftp(site, Dir = False):
    """
    lists contents of typical FTP download site

    Returns two lists, the first is of filenames, the second is of full filepaths
    (including filenames) that one could patch through to the "download_url" function.
    """
    
    ftp = ftplib.FTP(site)
    ftp.login()
    
    if Dir:
        ftp.cwd(Dir)
    else:
        ftp.cwd("")
        Dir = "" 
    
    rawdata = []
    ftp.dir(rawdata.append)
    filenames = [i.split()[-1] for i in rawdata[1:]]
    filepaths = ["ftp://"+"/".join([site,Dir,afile]).replace("//","/") for afile in filenames]
    return(filenames,filepaths)


def http(site):
    """Lists contents of typical http download site at [http://e4ftl01.cr.usgs.gov]"""
    
    website=urllib.urlopen(site)
    string=website.readlines()
    
    files=[]
    for line in string:
        try:files.append(line.replace('/','').split('"')[5])
        except: pass
    return files