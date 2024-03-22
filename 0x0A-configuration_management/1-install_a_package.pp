# 1-install_a_package.pp

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}

# Notify success message
notify { 'Flask installed successfully':
  subscribe => Exec['install_flask'],
}

