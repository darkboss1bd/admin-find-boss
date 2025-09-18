import requests
import argparse
import time
import sys

# Branding
BRAND = "DARKBOSS1BD"
TELEGRAM = "https://t.me/darkvaiadmin"
WEBSITE = "https://serialkey.top/"

# ASCII Hacker Logo
HACKER_LOGO = r"""
  ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗███████╗
  ██╔══██╗██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔═══██╗██╔════╝██╔════╝
  ██████╔╝███████║██║  ██║███████║██████╔╝██║   ██║███████╗█████╗  
  ██╔═══╝ ██╔══██║██║  ██║██╔══██║██╔═══╝ ██║   ██║╚════██║██╔══╝  
  ██║     ██║  ██║██████╔╝██║  ██║██║     ╚██████╔╝███████║███████╗
  ╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝
"""

# 300+ Admin Paths
ADMIN_PATHS = [
    "admin","administrator","admin/login","admin_panel","adminarea","admin1","admin2","admin3","admin4","admin5",
    "dashboard","backend","controlpanel","system","secure","siteadmin","webadmin","master","moderator","superadmin",
    "admin-console","manage","management","panel","console","root","private","secureadmin","secret","hidden",
    "login","login/admin","signin","sign-in","auth","authenticate","authentication","users/login","user/login",
    "member/login","members/login","portal","userpanel","session","access","gateway","connect",
    "wp-admin","wp-login.php","wp-content","wp-config.php","wp","wordpress","cms","joomla/administrator",
    "drupal/admin","typo3","umbraco","silverstripe","craft/admin","index.php/admin",
    "phpmyadmin","pma","dbadmin","mysql","myadmin","sql","database","db","sqlmanager","phpMyAdmin-4.9.7",
    "cpanel","whm","plesk","vesta","webmin","directadmin","ispconfig","server","server-status","status",
    "monitor","host",
    "shop/admin","store/admin","cart/admin","magento/admin","opencart/admin","prestashop/admin",
    "shopify/admin","woocommerce/admin","bigcommerce/admin",
    "admin.php","login.php","admin.html","admin.asp","admin.aspx","administrator.php","administrator.html",
    "backend.php","dashboard.php","home.php","index.php?admin","panel.php","admin.jsp","cp.php",
    "setup","install","config","configuration","init","bootstrap","install.php","setup.php",
    "config.php","upgrade.php","migrate",
    "api/admin","dev/admin","developer","debug","debugger","test/admin","staging/admin","qa/admin",
    "sandbox/admin",
    "admin_login","login_admin","signin_admin","adminsignin","adminsecure","security/admin","adminsecurity",
    "auth/admin","adminarea/login","admin-dashboard","dashboard/admin","admincontrol","controladmin",
    "superuser","godmode","root/admin",
    "mobile/admin","app/admin","admin_app","admin_mobile","m/admin","app/dashboard","mobile/dashboard",
    "api/dashboard",
    "analytics","stats","statistics","usage","report","reporting","metrics","tracking","logs","logging",
    "monitoring","audit",
    "backup","backups","restore","maintenance","maintenance-mode","update","upgrade","patch","hotfix",
    "systemupdate",
    "admin-secure","admin-protected","secure-login","2fa","authenticator","secureaccess","gatekeeper",
    "firewall","token","session/login",
    "hidden_admin","secret_admin","private_admin","hidden-login","hidden-panel","beta/admin","alpha/admin",
    "testpanel","testadmin","lab/admin","devpanel","internal/admin","internal/dashboard",
    "laravel-admin","nova","backoffice","erp/admin","crm/admin","helpdesk/admin","zendesk/admin",
    "jira/admin","bitrix/admin","suitecrm/admin","vTiger/admin","moodle/admin","canvas/admin",
    "grafana","kibana","zabbix","prometheus","jenkins","rundeck","nagios","cockpit","portainer",
    "netdata","elastic/admin",
    "adm","adm1n","adm!n","4dm1n","admin123","admin_123","dashboard123","panel123","access123",
    "secure123","login123","admin_test","test_admin","dev_admin","staging_login","beta_login",
    "oldadmin","old-admin","old_panel","legacyadmin","legacy_dashboard","v1/admin","v2/admin",
    "v3/admin","archive/admin","deprecated/admin"
]

def print_banner():
    print(f"\033[32m{HACKER_LOGO}\033[0m")
    print(f"\033[35m⚡ {BRAND} ADVANCED ADMIN FINDER ⚡\033[0m")
    print(f"\033[36mTelegram: {TELEGRAM} | Website: {WEBSITE}\033[0m")
    print("-" * 70)

def scan_panels(url):
    print(f"\033[33m🔥 [{BRAND}] Starting Scan on {url}\033[0m\n")
    total = len(ADMIN_PATHS)
    found_count = 0

    for i, path in enumerate(ADMIN_PATHS):
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url, timeout=5)
            status = response.status_code

            if status == 200:
                print(f"\033[32m[+] Found: {full_url} (200 OK)\033[0m")
                found_count += 1
            elif status == 403:
                print(f"\033[33m[!] Forbidden: {full_url} (403)\033[0m")
            elif status == 401:
                print(f"\033[33m[!] Unauthorized: {full_url} (401)\033[0m")
            elif status == 302:
                print(f"\033[36m[~] Redirected: {full_url} (302)\033[0m")
            else:
                print(f"\033[90m[-] Not Found: {full_url} ({status})\033[0m")

        except requests.exceptions.RequestException:
            print(f"\033[31m[x] Error connecting: {full_url}\033[0m")

        # Progress indicator
        progress = int((i + 1) / total * 50)
        bar = "█" * progress + "-" * (50 - progress)
        sys.stdout.write(f"\r\033[35mProgress: [{bar}] {i+1}/{total}\033[0m")
        sys.stdout.flush()

    print(f"\n\n\033[32m✅ Scan Completed! Total Admin Panels Found: {found_count}\033[0m")
    print(f"\033[35mTelegram: {TELEGRAM} | Website: {WEBSITE}\033[0m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Admin Panel Finder")
    parser.add_argument("url", help="Target website URL (e.g., https://example.com)")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        print("\033[31mError: URL must start with http:// or https://\033[0m")
        sys.exit(1)

    print_banner()
    scan_panels(args.url)
