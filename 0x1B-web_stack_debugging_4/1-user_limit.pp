#Updates the max open files limit for the holberton user

user { 'holberton':
  ensure => 'present',
  shell  => '/bin/bash',
  home   => '/home/holberton',
}

exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/sh -c "echo \"holberton soft nofile 4096\" >> /etc/security/limits.conf && \
              echo \"holberton hard nofile 4096\" >> /etc/security/limits.conf"',
  unless  => '/bin/grep -q "holberton soft nofile 4096" /etc/security/limits.conf && \
              /bin/grep -q "holberton hard nofile 4096" /etc/security/limits.conf',
}
