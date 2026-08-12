# Release Plan

## Release Philosophy
- stabilize architecture first
- release in narrow vertical slices
- avoid broad unfinished release scope
- release from an exact committed Integration/Release candidate
- run full applicable regression, security/accessibility, rollback and
  environment/package/deploy canaries
- reconcile current-state manifest and actual repository before and after merge
- require direct OWNER walkthrough only for ready release UI/device behavior;
  all automatable evidence remains manager-owned
