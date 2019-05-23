import sys
import os
import argparse

from datetime import datetime
import logging
import logging.handlers
import traceback

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

from yuktix import console
import yuktix.data.table.point as point_table



def print_sync_options(test_flag, api_wait, api_limit, endpoints):

    print "starting real time point sync program at {0}".format(datetime.now())
    print ""
    print " wait_time {0}, limit {1}, test flag {2}".format(api_wait, api_limit, test_flag)
    print u"\u001b[31m use --post to actually push data to  target server"
    print " use --wait and --limit to set api_wait time and api_limit"
    print u"\u001b[0m source:{0}, target:{1}".format(endpoints[0], endpoints[1])
    print ""
    print ""
    return





def main():

    log_config = console.get_config_section("logging")
    log_file = log_config["file"]
    log_level = log_config["level"]
    console.setup_logging({
        "level": log_level,
        "file" : log_file
    })

    logger = logging.getLogger("main." + _name_)

    parser = argparse.ArgumentParser(description='script to manage data archive synchronization.')
    parser.add_argument('--dump-tracker', action="store", dest="dump_file", help="dump file for point timestamps")
    parser.add_argument('--dump-archive', action="store", dest="dump_archive", help="dump file for archive timestamps")



    parser.add_argument('--load', action="store", dest="load_file", help="load point timestamps")
    parser.add_argument('--remove', action="store_true", help="remove point tracker row")
    parser.add_argument('--serial', action="store", dest="serial", help="serial number")
    parser.add_argument('--sync', action="store", help= "sync betwen source and target")
    parser.add_argument('--post', action="store_true", default=False)
    parser.add_argument('--wait', action="store", dest="wait", default=2.0)
    parser.add_argument('--limit', action="store", dest="limit", default=1000)
    parser.add_argument('--verbose', action="store_true", default=False)
    parser.add_argument('--db', action="store", dest="db_name", help="database to connect to")

    parser.add_argument("data", nargs=argparse.REMAINDER, help=argparse.SUPPRESS)

    options = parser.parse_args()
    database_name = options.db_name or "workerdb"

    # force debug logging
    if options.verbose:
        logger.setLevel(10)

    if options.dump_file:
        if os.path.exists(options.dump_file):
            parser.error("aborting! dump file already exists!")

    if options.dump_archive:
        if os.path.exists(options.dump_archive):
            parser.error("aborting! dump archive file already exists!")


    if options.load_file:
        if not os.path.exists(options.load_file):
            parser.error("aborting! load file not found!!!")


    if options.remove and not options.serial:
        parser.error("--remove option requires --serial option.")

    if options.sync:
        tokens = options.sync.split(":")
        if len(tokens) != 2:
           parser.error("aborting! --sync option should be in source:target format")


    db_config = console.get_config_section(database_name)
    api_wait = float(options.wait)
    api_limit = int(options.limit)
    connx = None

    try:

        connx = mysql.connector.connect(
                user=db_config["user"],
                password=db_config["password"],
                database=db_config["database"])

        connx.autocommit = False

        if options.remove:
            point_table.remove_timestamp(connx, serial=options.serial)
            print "removed point tracker timestamp row for {0}".format(options.serial)

        elif options.dump_file:
            point_table.dump_timestamp(connx, serial=options.serial, destination=options.dump_file)
            print "point tracker timestamps dumped to file {0}".format(options.dump_file)

        elif options.dump_archive:
            point_table.dump_archive_timestamp(connx, serial=options.serial, destination=options.dump_archive)
            print "point tracker timestamps dumped to file {0}".format(options.dump_archive)

        elif options.load_file:
            point_table.load_timestamp(connx, source=options.load_file, serial=options.serial, )
            print "point tracker timestamps import from {0} done!".format(options.load_file)



        elif options.sync:
            test_flag = True
            if options.post:
                test_flag = False

            endpoints = options.sync.split(":")
            print_sync_options(test_flag, api_wait, api_limit, endpoints)
            point_table.sync_data(connx,
                                    endpoints[0],
                                    endpoints[1],
                                    limit=api_limit,
                                    wait=api_wait,
                                    serial=options.serial,
                                    test=test_flag)
        else:
            parser.print_help()

        if connx:
            connx.close()

    except mysql.connector.Error as err:
        if connx:
            connx.rollback()
        print ("ERROR ::\r\n {0}".format(traceback.format_exc()))


    except Exception:
        print ("ERROR::\r\n {0}".format(traceback.format_exc()))


    return




if _name_ == '_main_':
    main()
