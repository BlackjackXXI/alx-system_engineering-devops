# 0-the_sky_is_the_limit_not.pp

# Adjust Nginx Configuration
exec { 'fix_for_nginx':
  command   => '/bin/sed -i "s/Document Length:        201 bytes/Document Length:        612 bytes/" /etc/nginx/nginx.conf',
  subscribe => File['/etc/nginx/nginx.conf'], # Update only when necessary
}

file { '/etc/nginx/nginx.conf':
  ensure => present,
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix_for_nginx'], # Restart Nginx after configuration is adjusted
}
