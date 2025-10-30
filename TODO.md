# TODO: Fix ESLint Errors

## Steps to Complete

- [ ] Create new file `frontend/src/hooks/useAuthHook.tsx` with the `useAuth` hook extracted from `useAuth.tsx`
- [ ] Update `frontend/src/hooks/useAuth.tsx` to remove unused `getDashboardPath` import and `useAuth` export, and import `useAuth` from the new file
- [ ] Update imports in the following files to import `useAuth` from `frontend/src/hooks/useAuthHook.tsx`:
  - frontend/src/pages/ClientDashboard.tsx
  - frontend/src/pages/ProviderDashboard.tsx
  - frontend/src/pages/Login.tsx
  - frontend/src/pages/ProfileRouter.tsx
  - frontend/src/pages/Home.tsx
  - frontend/src/components/__tests__/Login.test.tsx
  - frontend/src/components/__tests__/Navbar.test.tsx
  - frontend/src/components/ProtectedRoute.tsx
  - frontend/src/pages/ClientProfile.tsx
  - frontend/src/components/Navbar.tsx
  - frontend/src/pages/Profile.tsx
  - frontend/src/pages/ProviderProfile.tsx
- [ ] Edit `frontend/src/pages/Providers.tsx` to remove the unused `bookingData` parameter from `handleBookingSubmit`
- [ ] Edit `frontend/src/services/authService.ts` to remove the unused import of `ProviderSearchFilters`
- [ ] Run the linter to verify all errors are resolved
- [ ] Test the application to ensure functionality remains intact
