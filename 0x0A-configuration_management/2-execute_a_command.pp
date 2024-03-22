# Kills the process
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin']
}

