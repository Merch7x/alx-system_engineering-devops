# Fix Apache2 500 error

exec { 'Fix-doc-root':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
