file { '/etc/security/limits.conf':
  ensure  => present,
  content => template('my_module/limits.conf.erb'),
}

augeas { 'increase-holberton-file-limits':
  context => '/files/etc/security/limits.conf',
  changes => [
    'set user[. = "holberton"]/hard 50000',
    'set user[. = "holberton"]/soft 50000',
  ],
}

