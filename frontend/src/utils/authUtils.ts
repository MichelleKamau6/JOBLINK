export function getDashboardPath(user: { role: string } | null): string {
  if (!user) return '/';
  if (user.role === 'admin') return '/dashboard';
  if (user.role === 'provider') return '/provider-dashboard';
  return '/client-dashboard';
}
