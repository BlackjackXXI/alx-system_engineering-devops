# find out why Apache is returning a 500 error and fix it

exec { 'error_500_fix':
  command    => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path       => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
