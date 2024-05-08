# find out why Apache is returning a 500 error and fix it

exec { 'fix config typo':
  path       => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command    => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
}
