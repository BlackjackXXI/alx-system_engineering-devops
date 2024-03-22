# Install flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'flask-installer':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
}

