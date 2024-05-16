# 1-user_limit.pp

exec { 'change-os-configuration-for-holberton-user':
  command  => "ulimit -n 15000 && sed -i 's/^session    required     pam_limits.so/#session    required     pam_limits.so/' /etc/pam.d/common-session",
  provider => 'shell',
}
