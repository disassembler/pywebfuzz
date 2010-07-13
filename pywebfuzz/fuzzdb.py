#!/usr/bin/env python
import os
import sys

MODPATH = os.path.dirname(__file__)

class attack_payloads:
    """ Placeholder namespace for the attack_payloads"""
    class all_attacks:
        """ This implements the all-attacks from fuzzdb """
        
        # all-attacks-unix.txt
        location = "/data/attack-payloads/all-attacks/all-attacks-unix.txt"

        path = MODPATH + location

        file = open(path, "rb")
        all_attacks_unix = list()
        for item in file.readlines():
            all_attacks_unix.append(item.rstrip())
            
        file.close()
        
        # all-attacks-win.txt
        location = "/data/attack-payloads/all-attacks/all-attacks-win.txt"
        
        path = MODPATH + location
        file = open(path, "rb")
        all_attacks_win = list()
        for item in file.readlines():
            all_attacks_win.append(item.rstrip())
        file.close()
        
        # interesting-metacharacters.txt
        location = "/data/attack-payloads/all-attacks/interesting-metacharacters.txt"
        
        path = MODPATH + location
        file = open(path, "rb")
        interesting_metacharacters = list()
        for item in file.readlines():
            interesting_metacharacters.append(item.rstrip())
        file.close()
        
    class disclosure_directory:
        """ This implements the disclosure-directory from fuzzdb """
        
        class generic:
            """ generic payloads """
            
            # directory-indexing-generic.txt
            location = "/data/attack-payloads/disclosure-directory/generic/directory-indexing-generic.txt"

            path = MODPATH + location

            file = open(path, "rb")
            directory_indexing_generic = list()
            for item in file.readlines():
                directory_indexing_generic.append(item.rstrip())
            
            file.close()
        
        class unix:
            """ unix payloads """
            # This class is currently empty
        
        class win:
            """ win payloads """
            # This class is currently empty
            
    class disclosure_localpaths:
        """ This implements the disclosure-localpaths from fuzzdb """
        
        class microsoft:
            """ microsoft """
            # This class is currently empty
        
        class unix:
            """ unix """
            
            # common-unix-httpd-log-locations.txt
            location = "/data/attack-payloads/disclosure-localpaths/unix/common-unix-httpd-log-locations.txt"

            path = MODPATH + location

            file = open(path, "rb")
            common_unix_httpd_log_locations = list()
            for item in file.readlines():
                common_unix_httpd_log_locations.append(item.rstrip())
            
            file.close()
            
    class disclosure_source:
        """ This implements the disclosure-source from fuzzdb """
        
        # source-disc-cmd-exec-traversal
        location = "/data/attack-payloads/disclosure-source/source-disc-cmd-exec-traversal.txt"

        path = MODPATH + location

        file = open(path, "rb")
        source_disc_cmd_exec_traversal = list()
        for item in file.readlines():
           source_disc_cmd_exec_traversal.append(item.rstrip())
            
        file.close()
        
        # source-disclosure-generic.txt
        location = "/data/attack-payloads/disclosure-source/source-disclosure-generic.txt"

        path = MODPATH + location

        file = open(path, "rb")
        source_disclosure_generic = list()
        for item in file.readlines():
           source_disclosure_generic.append(item.rstrip())
            
        file.close()
        
        # source-disclosure-microsoft.txt
        location = "/data/attack-payloads/disclosure-source/source-disclosure-microsoft.txt"

        path = MODPATH + location

        file = open(path, "rb")
        source_disclosure_microsoft = list()
        for item in file.readlines():
           source_disclosure_microsoft.append(item.rstrip())
            
        file.close()
        
    class file_upload:
        """ This implements the file-upload from fuzzdb """
        
        # alt-extensions-asp.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-asp.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        alt_extensions_asp = list()
        for item in file.readlines():
           alt_extensions_asp.append(item.rstrip())
            
        file.close()
        
        # alt-extensions-coldfusion.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-coldfusion.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        alt_extensions_coldfusion = list()
        for item in file.readlines():
           alt_extensions_coldfusion.append(item.rstrip())
            
        file.close()
        
        # alt-extensions-jsp.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-jsp.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        alt_extensions_jsp = list()
        for item in file.readlines():
           alt_extensions_jsp.append(item.rstrip())
            
        file.close()
        
        # alt-extensions-perl.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-perl.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        alt_extensions_perl = list()
        for item in file.readlines():
           alt_extensions_perl.append(item.rstrip())
            
        file.close()
        
        # alt-extensions-php.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-php.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        alt_extensions_php = list()
        for item in file.readlines():
           alt_extensions_php.append(item.rstrip())
            
        file.close()
        
        # file-ul-filter-bypass-commonly-writable-directories.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-commonly-writable-directories.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        file_ul_filter_bypass_commonly_writable_directories = list()
        for item in file.readlines():
           file_ul_filter_bypass_commonly_writable_directories.append(item.rstrip())
            
        file.close()
        
        # file-ul-filter-bypass-microsoft-asp-filetype-bf.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-microsoft-asp-filetype-bf.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        file_ul_filter_bypass_microsoft_asp_filetype_bf = list()
        for item in file.readlines():
           file_ul_filter_bypass_microsoft_asp_filetype_bf.append(item.rstrip())
            
        file.close()
        
        # file-ul-filter-bypass-microsoft-asp.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-microsoft-asp.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        file_ul_filter_bypass_microsoft_asp = list()
        for item in file.readlines():
           file_ul_filter_bypass_microsoft_asp.append(item.rstrip())
            
        file.close()
        
        # file-ul-filter-bypass-ms-php.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-ms-php.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        file_ul_filter_bypass_ms_php = list()
        for item in file.readlines():
           file_ul_filter_bypass_ms_php.append(item.rstrip())
            
        file.close()
        
        # file-ul-filter-bypass-x-platform-generic.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-x-platform-generic.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        file_ul_filter_bypass_x_platform_generic = list()
        for item in file.readlines():
           file_ul_filter_bypass_x_platform_generic.append(item.rstrip())
            
        file.close()
        
        # file-ul-filter-bypass-x-platform-php.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-x-platform-php.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        file_ul_filter_bypass_x_platform_php = list()
        for item in file.readlines():
           file_ul_filter_bypass_x_platform_php.append(item.rstrip())
            
        file.close()
        
        # invalid-filenames-linux.txt
        location = "/data/attack-payloads/file-upload/invalid-filenames-linux.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        invalid_filenames_linux = list()
        for item in file.readlines():
           invalid_filenames_linux.append(item.rstrip())
            
        file.close()
        
        # invalid-filenames-microsoft.txt
        location = "/data/attack-payloads/file-upload/invalid-filenames-microsoft.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        invalid_filenames_microsoft = list()
        for item in file.readlines():
           invalid_filenames_microsoft.append(item.rstrip())
            
        file.close()
        
        # invalid-filesystem-chars-microsoft.txt
        location = "/data/attack-payloads/file-upload/invalid-filesystem-chars-microsoft.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        invalid_filesystem_chars_microsoft = list()
        for item in file.readlines():
           invalid_filesystem_chars_microsoft.append(item.rstrip())
            
        file.close()
        
        # invalid-filesystem-chars-osx.txt
        location = "/data/attack-payloads/file-upload/invalid-filesystem-chars-osx.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        invalid_filesystem_chars_osx = list()
        for item in file.readlines():
           invalid_filesystem_chars_osx.append(item.rstrip())
            
        file.close()
        
    class format_strings:
        """ This implements the format-strings from fuzzdb """
        
        # format-strings.txt
        location = "/data/attack-payloads/format-strings/format-strings.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        format_strings = list()
        for item in file.readlines():
           format_strings.append(item.rstrip())
            
        file.close()
        
    class http_protocol:
        """ This implements the http-protocol from fuzzdb """
        
        # format-strings.txt
        location = "/data/attack-payloads/http-protocol/http-header-cache-poison.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        http_header_cache_poison = list()
        for item in file.readlines():
           http_header_cache_poison.append(item.rstrip())
            
        file.close()
        
        # http-protocol-methods.txt
        location = "/data/attack-payloads/http-protocol/http-protocol-methods.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        http_protocol_methods = list()
        for item in file.readlines():
           http_protocol_methods.append(item.rstrip())
            
        file.close()
        
        # user-agents.txt
        location = "/data/attack-payloads/http-protocol/user-agents.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        user_agents = list()
        for item in file.readlines():
           user_agents.append(item.rstrip())
            
        file.close()
        
    class integer_overflow:
        """ This implements the integer-overflow from fuzzdb """
        
        # integer-overflow.txt
        location = "/data/attack-payloads/integer-overflow/integer-overflows.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        integer_overflows = list()
        for item in file.readlines():
           integer_overflows.append(item.rstrip())
            
        file.close()
        
    class ldap:
        
        # ldap-injection.txt
        location = "/data/attack-payloads/ldap/ldap-injection.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        ldap_injection = list()
        for item in file.readlines():
           ldap_injection.append(item.rstrip())
            
        file.close()
        
    class lfi:
        
        # common-unix-httpd-log-locations.txt
        location = "/data/attack-payloads/lfi/common-unix-httpd-log-locations.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        common_unix_httpd_log_locations = list()
        for item in file.readlines():
           common_unix_httpd_log_locations.append(item.rstrip())
            
        file.close()
        
    class os_cmd_execution:
        
        # command-execution-unix.txt
        location = "/data/attack-payloads/os-cmd-execution/command-execution-unix.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        command_execution_unix = list()
        for item in file.readlines():
           command_execution_unix.append(item.rstrip())
            
        file.close()
        
        # commands-unix.txt
        location = "/data/attack-payloads/os-cmd-execution/commands-unix.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        commands_unix = list()
        for item in file.readlines():
           commands_unix.append(item.rstrip())
            
        file.close()
        
        # commands-windows.txt
        location = "/data/attack-payloads/os-cmd-execution/commands-windows.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        commands_windows = list()
        for item in file.readlines():
           commands_windows.append(item.rstrip())
            
        file.close()
        
        # source-disc-cmd-exec-traversal.txt
        location = "/data/attack-payloads/os-cmd-execution/source-disc-cmd-exec-traversal.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        source_disc_cmd_exec_traversal = list()
        for item in file.readlines():
           source_disc_cmd_exec_traversal.append(item.rstrip())
            
        file.close()
        
    class os_dir_indexing:
        
        # directory-indexing.txt
        location = "/data/attack-payloads/os-dir-indexing/directory-indexing.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        directory_indexing = list()
        for item in file.readlines():
           directory_indexing.append(item.rstrip())
            
        file.close()
        
    class path_traversal:
        
        # directory-indexing.txt
        location = "/data/attack-payloads/path-traversal/path-traversal-windows.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        path_traversal_windows = list()
        for item in file.readlines():
           path_traversal_windows.append(item.rstrip())
            
        file.close()
        
        # traversals-8-deep-exotic-encoding.txt
        location = "/data/attack-payloads/path-traversal/traversals-8-deep-exotic-encoding.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        traversals_8_deep_exotic_encoding = list()
        for item in file.readlines():
           traversals_8_deep_exotic_encoding.append(item.rstrip())
            
        file.close()
        
    class rfi:
        
        # rfi.txt
        location = "/data/attack-payloads/rfi/rfi.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        rfi = list()
        for item in file.readlines():
           rfi.append(item.rstrip())
            
        file.close()
        
    class server_side_include:
        
        # server-side-includes-generic.txt
        location = "/data/attack-payloads/server-side-include/server-side-includes-generic.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        server_side_includes_generic = list()
        for item in file.readlines():
           server_side_includes_generic.append(item.rstrip())
            
        file.close()
        
    class sql_injection:
        
        class detect:
            
            class generic:
                
               # sql-injection-active.txt
                location = "/data/attack-payloads/sql-injection/detect/generic/sql-injection-active.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection_active = list()
                for item in file.readlines():
                   sql_injection_active.append(item.rstrip())
            
                file.close()
                
                
                # sql-injection-passive.txt
                location = "/data/attack-payloads/sql-injection/detect/generic/sql-injection-passive.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection_passive = list()
                for item in file.readlines():
                   sql_injection_passive.append(item.rstrip())
            
                file.close()
                
                # sql-injection.txt
                location = "/data/attack-payloads/sql-injection/detect/generic/sql-injection.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection = list()
                for item in file.readlines():
                   sql_injection.append(item.rstrip())
            
                file.close()
                
            class ms_sql:
                
                # sql-injection-ms-sql-blind-ninja.txt
                location = "/data/attack-payloads/sql-injection/detect/ms-sql/sql-injection-ms-sql-blind-ninja.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection_ms_sql_blind_ninja = list()
                for item in file.readlines():
                   sql_injection_ms_sql_blind_ninja.append(item.rstrip())
            
                file.close()
                
                # sql-injection-ms-sql.txt
                location = "/data/attack-payloads/sql-injection/detect/ms-sql/sql-injection-ms-sql.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection_ms_sql = list()
                for item in file.readlines():
                   sql_injection_ms_sql.append(item.rstrip())
            
                file.close()
                
            class mysql:
                
                # sql-injection-mysql-ms-sql.txt
                location = "/data/attack-payloads/sql-injection/detect/mysql/sql-injection-mysql-ms-sql.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection_mysql_ms_sql = list()
                for item in file.readlines():
                   sql_injection_mysql_ms_sql.append(item.rstrip())
            
                file.close()
                
                # sql-injection-mysql.txt
                location = "/data/attack-payloads/sql-injection/detect/mysql/sql-injection-mysql.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection_mysql = list()
                for item in file.readlines():
                   sql_injection_mysql.append(item.rstrip())
            
                file.close()
                
            class oracle:
                
                # sql-injection-oracle.txt
                location = "/data/attack-payloads/sql-injection/detect/oracle/sql-injection-oracle.txt"
        
                path = MODPATH + location

                file = open(path, "rb")
                sql_injection_oracle = list()
                for item in file.readlines():
                   sql_injection_oracle.append(item.rstrip())
            
                file.close()
                
        class exploit:
            
            # db2-enumeration.txt
            location = "/data/attack-payloads/sql-injection/exploit/db2-enumeration.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            db2_enumeration = list()
            for item in file.readlines():
               db2_enumeration.append(item.rstrip())
            
            file.close()
            
            # ms-sql-enumeration.txt
            location = "/data/attack-payloads/sql-injection/exploit/ms-sql-enumeration.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            ms_sql_enumeration = list()
            for item in file.readlines():
               ms_sql_enumeration.append(item.rstrip())
            
            file.close()
            
            # mysql-injection-login-bypass.txt
            location = "/data/attack-payloads/sql-injection/exploit/mysql-injection-login-bypass.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            mysql_injection_login_bypass = list()
            for item in file.readlines():
               mysql_injection_login_bypass.append(item.rstrip())
            
            file.close()
            
            # mysql-read-local-files.txt
            location = "/data/attack-payloads/sql-injection/exploit/mysql-read-local-files.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            mysql_read_local_files = list()
            for item in file.readlines():
               mysql_read_local_files.append(item.rstrip())
            
            file.close()
            
            # postgres-enumeration.txt
            location = "/data/attack-payloads/sql-injection/exploit/postgres-enumeration.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            postgres_enumeration = list()
            for item in file.readlines():
               postgres_enumeration.append(item.rstrip())
            
            file.close()
            
    class xml:
        
        # xml-attacks.txt
        location = "/data/attack-payloads/xml/xml-attacks.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        xml_attacks = list()
        for item in file.readlines():
           xml_attacks.append(item.rstrip())
            
        file.close()
        
    class xpath:
        
        # xpath-injection.txt
        location = "/data/attack-payloads/xpath/xpath-injection.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        xpath_injection = list()
        for item in file.readlines():
           xpath_injection.append(item.rstrip())
            
        file.close()
        
    class xss:
        
        # xss-rsnake.txt
        location = "/data/attack-payloads/xss/xss-rsnake.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        xss_rsnake = list()
        for item in file.readlines():
           xss_rsnake.append(item.rstrip())
            
        file.close()
        
        # xss-uri.txt
        location = "/data/attack-payloads/xss/xss-uri.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        xss_uri = list()
        for item in file.readlines():
           xss_uri.append(item.rstrip())
            
        file.close()
        
class discovery:
    
    class filename_bruteforce:
        
        class file_extensions:
            
            
            # file-extensions-backup-files.txt
            location = "/data/discovery/filename-bruteforce/file-extensions/file-extensions-backup-files.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            file_extensions_backup_files = list()
            for item in file.readlines():
               file_extensions_backup_files.append(item.rstrip())
            
            file.close()
            
            # file-extensions-common-datafile-types.txt
            location = "/data/discovery/filename-bruteforce/file-extensions/file-extensions-common-datafile-types.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            file_extensions_common_datafile_types = list()
            for item in file.readlines():
               file_extensions_common_datafile_types.append(item.rstrip())
            
            file.close()
            
            # file-extensions-compressed-filetypes.txt
            location = "/data/discovery/filename-bruteforce/file-extensions/file-extensions-compressed-filetypes.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            file_extensions_compressed_filetypes = list()
            for item in file.readlines():
               file_extensions_compressed_filetypes.append(item.rstrip())
            
            file.close()
            
            # file-extensions-mostcommon.txt
            location = "/data/discovery/filename-bruteforce/file-extensions/file-extensions-mostcommon.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            file_extensions_mostcommon = list()
            for item in file.readlines():
               file_extensions_mostcommon.append(item.rstrip())
            
            file.close()
            
            # file-extensions-skipfish.txt
            location = "/data/discovery/filename-bruteforce/file-extensions/file-extensions-skipfish.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            file_extensions_skipfish = list()
            for item in file.readlines():
               file_extensions_skipfish.append(item.rstrip())
            
            file.close()
            
        class file_or_dir_root_wordlists:
            
            # wordlist-skipfish.txt
            location = "/data/discovery/filename-bruteforce/file-or-dir-root-wordlists/wordlist-skipfish.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            wordlist_skipfish = list()
            for item in file.readlines():
               wordlist_skipfish.append(item.rstrip())
            
            file.close()
            
    class generic:
        
        class cms:
            
            # drupal_plugins.txt
            location = "/data/discovery/generic/cms/drupal_plugins.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            drupal_plugins = list()
            for item in file.readlines():
               drupal_plugins.append(item.rstrip())
            
            file.close()
            
            # drupal_themes.txt
            location = "/data/discovery/generic/cms/drupal_themes.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            drupal_themes = list()
            for item in file.readlines():
               drupal_themes.append(item.rstrip())
            
            file.close()
            
            # joomla_plugins.txt
            location = "/data/discovery/generic/cms/joomla_plugins.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            joomla_plugins = list()
            for item in file.readlines():
               joomla_plugins.append(item.rstrip())
            
            file.close()
            
            # joomla_themes.txt
            location = "/data/discovery/generic/cms/joomla_themes.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            joomla_themes = list()
            for item in file.readlines():
               joomla_themes.append(item.rstrip())
            
            file.close()
            
            # wp_plugins.txt
            location = "/data/discovery/generic/cms/wp_plugins.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            wp_plugins = list()
            for item in file.readlines():
               wp_plugins.append(item.rstrip())
            
            file.close()
            
            # wp_themes.txt
            location = "/data/discovery/generic/cms/wp_themes.txt"
        
            path = MODPATH + location

            file = open(path, "rb")
            wp_themes = list()
            for item in file.readlines():
               wp_themes.append(item.rstrip())
            
            file.close()
            
        # cgi-HTTP-POST-reqd.txt
        location = "/data/discovery/generic/cgi-HTTP-POST-reqd.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        cgi_HTTP_POST_reqd = list()
        for item in file.readlines():
           cgi_HTTP_POST_reqd.append(item.rstrip())
            
        file.close()
        
        # cgi-x-platform.txt
        location = "/data/discovery/generic/cgi-x-platform.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        cgi_x_platform = list()
        for item in file.readlines():
           cgi_x_platform.append(item.rstrip())
            
        file.close()
        
        # interesting-dirs-kitchensink.txt
        location = "/data/discovery/generic/interesting-dirs-kitchensink.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_dirs_kitchensink = list()
        for item in file.readlines():
           interesting_dirs_kitchensink.append(item.rstrip())
            
        file.close()
        
        # interesting-files-apache-tomcat.txt
        location = "/data/discovery/generic/interesting-files-apache-tomcat.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_apache_tomcat = list()
        for item in file.readlines():
           interesting_files_apache_tomcat.append(item.rstrip())
            
        file.close()
        
        # interesting-files-apache.txt
        location = "/data/discovery/generic/interesting-files-apache.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_apache = list()
        for item in file.readlines():
           interesting_files_apache.append(item.rstrip())
            
        file.close()
        
        # interesting-files-coldfusion.txt
        location = "/data/discovery/generic/interesting-files-coldfusion.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_coldfusion = list()
        for item in file.readlines():
           interesting_files_coldfusion.append(item.rstrip())
            
        file.close()
        
        # interesting-files-hyperion.txt
        location = "/data/discovery/generic/interesting-files-hyperion.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_hyperion = list()
        for item in file.readlines():
           interesting_files_hyperion.append(item.rstrip())
            
        file.close()
        
        # interesting-files-logins.txt
        location = "/data/discovery/generic/interesting-files-logins.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_logins = list()
        for item in file.readlines():
           interesting_files_logins.append(item.rstrip())
            
        file.close()
        
        # interesting-files-lotus-notes.txt
        location = "/data/discovery/generic/interesting-files-lotus-notes.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_lotus_notes = list()
        for item in file.readlines():
           interesting_files_lotus_notes.append(item.rstrip())
            
        file.close()
        
        # interesting-files-oracle-application-server.txt
        location = "/data/discovery/generic/interesting-files-oracle-application-server.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_oracle_application_server = list()
        for item in file.readlines():
           interesting_files_oracle_application_server.append(item.rstrip())
            
        file.close()
        
        # interesting-files-passwords.txt
        location = "/data/discovery/generic/interesting-files-passwords.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_passwords = list()
        for item in file.readlines():
           interesting_files_passwords.append(item.rstrip())
            
        file.close()
        
        # interesting-files-random.txt
        location = "/data/discovery/generic/interesting-files-random.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_random = list()
        for item in file.readlines():
           interesting_files_random.append(item.rstrip())
            
        file.close()
        
        # interesting-files-websphere.txt
        location = "/data/discovery/generic/interesting-files-websphere.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_websphere = list()
        for item in file.readlines():
           interesting_files_websphere.append(item.rstrip())
            
        file.close()
        
        # php-common-backdoors.txt
        location = "/data/discovery/generic/php-common-backdoors.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        php_common_backdoors = list()
        for item in file.readlines():
           php_common_backdoors.append(item.rstrip())
            
        file.close()
        
        # tftp.txt
        location = "/data/discovery/generic/tftp.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        tftp = list()
        for item in file.readlines():
           tftp.append(item.rstrip())
            
        file.close()
        
    class unix:
        
        # interesting-files-dotfiles.txt
        location = "/data/discovery/unix/interesting-files-dotfiles.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_dotfiles = list()
        for item in file.readlines():
           interesting_files_dotfiles.append(item.rstrip())
            
        file.close()
        
        # interesting-files-iplanet.txt
        location = "/data/discovery/unix/interesting-files-dotfiles.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_iplanet = list()
        for item in file.readlines():
           interesting_files_iplanet.append(item.rstrip())
            
        file.close()
        
        # interesting-files-sun-app-server.txt
        location = "/data/discovery/unix/interesting-files-sun-app-server.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_sun_app_server = list()
        for item in file.readlines():
           interesting_files_sun_app_server.append(item.rstrip())
            
        file.close()
        
    class win:
        
        # cgi-HTTP-POST-reqd-microsoft.txt
        location = "/data/discovery/win/cgi-HTTP-POST-reqd-microsoft.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        cgi_HTTP_POST_reqd_microsoft = list()
        for item in file.readlines():
           cgi_HTTP_POST_reqd_microsoft.append(item.rstrip())
            
        file.close()
        
        # cgi-microsoft.txt
        location = "/data/discovery/win/cgi-microsoft.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        cgi_microsoft = list()
        for item in file.readlines():
           cgi_microsoft.append(item.rstrip())
            
        file.close()
        
        # interesting-files-microsoft-iis-http-post.txt
        location = "/data/discovery/win/interesting-files-microsoft-iis-http-post.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_microsoft_iis_http_post = list()
        for item in file.readlines():
           interesting_files_microsoft_iis_http_post.append(item.rstrip())
            
        file.close()
        
        # interesting-files-microsoft-iis.txt
        location = "/data/discovery/win/interesting-files-microsoft-iis.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_microsoft_iis = list()
        for item in file.readlines():
           interesting_files_microsoft_iis.append(item.rstrip())
            
        file.close()
        
        # interesting-files-microsoft-sharepoint.txt
        location = "/data/discovery/win/interesting-files-microsoft-sharepoint.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_microsoft_sharepoint = list()
        for item in file.readlines():
           interesting_files_microsoft_sharepoint.append(item.rstrip())
            
        file.close()
        
        # interesting-files-netware.txt
        location = "/data/discovery/win/interesting-files-netware.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        interesting_files_netware = list()
        for item in file.readlines():
           interesting_files_netware.append(item.rstrip())
            
        file.close()
        
class regex:
    
    # errors.txt
    location = "/data/regex/errors.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    errors = list()
    for item in file.readlines():
       errors.append(item.rstrip())
        
    file.close()
    
    # sessionid.txt
    location = "/data/regex/sessionid.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    sessionid = list()
    for item in file.readlines():
       sessionid.append(item.rstrip())
        
    file.close()
    
class wordlists_misc:
    
    # common-http-ports.txt
    location = "/data/wordlists-misc/common-http-ports.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    common_http_ports = list()
    for item in file.readlines():
       common_http_ports.append(item.rstrip())
        
    file.close()
    
    # us_cities.txt
    location = "/data/wordlists-misc/us_cities.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    us_cities = list()
    for item in file.readlines():
       us_cities.append(item.rstrip())
        
    file.close()
    
    # wordlist-alphanumeric-case.txt
    location = "/data/wordlists-misc/wordlist-alphanumeric-case.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    wordlist_alphanumeric_case = list()
    for item in file.readlines():
       wordlist_alphanumeric_case.append(item.rstrip())
        
    file.close()
    
    # wordlist-common-snmp-community-strings.txt
    location = "/data/wordlists-misc/wordlist-alphanumeric-case.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    wordlist_common_snmp_community_strings = list()
    for item in file.readlines():
       wordlist_common_snmp_community_strings.append(item.rstrip())
        
    file.close()
    
    # wordlist-dna.txt
    location = "/data/wordlists-misc/wordlist-dna.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    wordlist_dna = list()
    for item in file.readlines():
       wordlist_dna.append(item.rstrip())
        
    file.close()
    
class wordlists_user_passwd:
    
    class db2:
        
        # db2_default_pass.txt
        location = "/data/wordlists-user-passwd/db2/db2_default_pass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        db2_default_pass = list()
        for item in file.readlines():
           db2_default_pass.append(item.rstrip())
            
        file.close()
        
        # db2_default_user.txt
        location = "/data/wordlists-user-passwd/db2/db2_default_user.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        db2_default_user = list()
        for item in file.readlines():
           db2_default_user.append(item.rstrip())
            
        file.close()
        
        # db2_default_userpass.txt
        location = "/data/wordlists-user-passwd/db2/db2_default_userpass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        db2_default_userpass = list()
        for item in file.readlines():
           db2_default_userpass.append(item.rstrip())
            
        file.close()
        
    class generic_listpairs:
        
        # http_default_pass.txt
        location = "/data/wordlists-user-passwd/generic-listpairs/http_default_pass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        http_default_pass = list()
        for item in file.readlines():
           http_default_pass.append(item.rstrip())
            
        file.close()
        
        # http_default_userpass.txt
        location = "/data/wordlists-user-passwd/generic-listpairs/http_default_userpass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        http_default_userpass = list()
        for item in file.readlines():
           http_default_userpass.append(item.rstrip())
            
        file.close()
        
        # http_default_users.txt
        location = "/data/wordlists-user-passwd/generic-listpairs/http_default_users.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        http_default_users = list()
        for item in file.readlines():
           http_default_users.append(item.rstrip())
            
        file.close()
        
    class names:
        
        # namelist.txt
        location = "/data/wordlists-user-passwd/names/namelist.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        namelist = list()
        for item in file.readlines():
           namelist.append(item.rstrip())
            
        file.close()
        
    class oracle:
        
        # _hci_oracle_passwords.txt
        location = "/data/wordlists-user-passwd/oracle/_hci_oracle_passwords.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        _hci_oracle_passwords = list()
        for item in file.readlines():
           _hci_oracle_passwords.append(item.rstrip())
            
        file.close()
        
        # _oracle_default_passwords.txt
        location = "/data/wordlists-user-passwd/oracle/_oracle_default_passwords.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        _oracle_default_passwords = list()
        for item in file.readlines():
           _oracle_default_passwords.append(item.rstrip())
            
        file.close()
        
    class passwds:
        
        # john.txt
        location = "/data/wordlists-user-passwd/passwds/john.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        john = list()
        for item in file.readlines():
           john.append(item.rstrip())
            
        file.close()
        
        # phpbb.txt
        location = "/data/wordlists-user-passwd/passwds/phpbb.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        phpbb = list()
        for item in file.readlines():
           phpbb.append(item.rstrip())
            
        file.close()
        
        # twitter.txt
        location = "/data/wordlists-user-passwd/passwds/twitter.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        twitter = list()
        for item in file.readlines():
           twitter.append(item.rstrip())
            
        file.close()
        
        # weaksauce.txt
        location = "/data/wordlists-user-passwd/passwds/weaksauce.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        weaksauce = list()
        for item in file.readlines():
           weaksauce.append(item.rstrip())
            
        file.close()
        
    class postgres:
        
        # postgres_default_pass.txt
        location = "/data/wordlists-user-passwd/postgres/postgres_default_pass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        postgres_default_pass = list()
        for item in file.readlines():
           postgres_default_pass.append(item.rstrip())
            
        file.close()
        
        # postgres_default_user.txt
        location = "/data/wordlists-user-passwd/postgres/postgres_default_user.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        postgres_default_user = list()
        for item in file.readlines():
           postgres_default_user.append(item.rstrip())
            
        file.close()
        
        # postgres_default_userpass.txt
        location = "/data/wordlists-user-passwd/postgres/postgres_default_userpass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        postgres_default_userpass = list()
        for item in file.readlines():
           postgres_default_userpass.append(item.rstrip())
            
        file.close()
        
    class tomcat:
        
        # tomcat_mgr_default_pass.txt
        location = "/data/wordlists-user-passwd/tomcat/tomcat_mgr_default_pass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        tomcat_mgr_default_pass = list()
        for item in file.readlines():
           tomcat_mgr_default_pass.append(item.rstrip())
            
        file.close()
        
        # tomcat_mgr_default_userpass.txt
        location = "/data/wordlists-user-passwd/tomcat/tomcat_mgr_default_userpass.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        tomcat_mgr_default_userpass = list()
        for item in file.readlines():
           tomcat_mgr_default_userpass.append(item.rstrip())
            
        file.close()
        
        # tomcat_mgr_default_users.txt
        location = "/data/wordlists-user-passwd/tomcat/tomcat_mgr_default_users.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        tomcat_mgr_default_users = list()
        for item in file.readlines():
           tomcat_mgr_default_users.append(item.rstrip())
            
        file.close()
        
    class unix_os:
        
        # unix_passwords.txt
        location = "/data/wordlists-user-passwd/unix-os/unix_passwords.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        unix_passwords = list()
        for item in file.readlines():
           unix_passwords.append(item.rstrip())
            
        file.close()
        
        # unix_users.txt
        location = "/data/wordlists-user-passwd/unix-os/unix_users.txt"
        
        path = MODPATH + location

        file = open(path, "rb")
        unix_users = list()
        for item in file.readlines():
           unix_users.append(item.rstrip())
            
        file.close()
        
    # faithwriters.txt
    location = "/data/wordlists-user-passwd/faithwriters.txt"
        
    path = MODPATH + location

    file = open(path, "rb")
    faithwriters = list()
    for item in file.readlines():
       faithwriters.append(item.rstrip())
        
    file.close()
    