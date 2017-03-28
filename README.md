# Monit ansible role

Installs and configures monit.

This role also includes an sms alerting scipt which uses twilio as the sms service provider.

## MMonit + Monit architecture
Monit pushes stats to mmonit periodically, and on events.
We will use self signed certificates for

## Mandatory variables
* monit_admin_mails: Mail addresses, which alerts are sent to.
* monit_basic_configs: Basic config files to use. This config files are include with the role.
* monit_admin_group: Name of the monit admin group.
* monit_twilio: Do you want to use twilio for alerts
* monit_mmonit_licence: MMonit server licence.

## Optional variables

* monit_custom_config_directory: Directory where you have your own monit configs defined.
* monit_custom_configs: Which monit configs to include from the custom location.
* monit_twilio_account: Your twilio account ID.
* monit_twilio_auh_token: Your twilio auth token.
* monit_twilio_number_to: Which number to send sms alerts to. Make sure it's configured on twilio to work fot this number if you're using a trial account.
* monit_twilio_number_from: hich phone number to send sms alerts from.
* monit_mmonit: Send metrics to mmonit (True|False)
* monit_mmonit_master: Setup mmonit instance
* monit_mmonit_port: MMonit local port
* monit_mmonit_version:  Which version of mmonit t install
* monit_mmonit_password: Monit user password - for sending metrics
* monit_mmonit_username: Monit username - for sending metrics
* monit_mmonit_group: Monit user group
* monit_mmonit_hostname: Mmonit server address(with http and all)
* monit_mmonit_proxy_port: Mmonit server name as seen from outside.
* monit_mmonit_proxy_name: Name of the server as seen from the outside
* monit_mmonit_pemfile: Path to monit certificate pemfile
* monit_mmonit_host_ip: mmonit host ip

## MMonit
To use mmonit, set `monit_mmonit` to true. Other than that, you need to set the monit_mmonit_port.
