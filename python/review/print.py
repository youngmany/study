# Separator Option
print('T', 'E', 'S', 'T', sep='')
print('2019', '09', '30', sep='-')
print('ymkim', 'google.com', sep='@')

# End Option
print('Young', end=' ')
print('Many', end=' ')
print('Kim')

# format Option
print('{} ~ {}'.format('Young', 'Many'))
print("{0} and {1} and {0}".format('Young', 'Many'))
print("{a} are {b}".format(a="young", b='many'))

print('%s %d' % ('test', 7))

# escape
print('\'A\'')