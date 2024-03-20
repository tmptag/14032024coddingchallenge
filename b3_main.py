from sqlalchemy.orm import joinedload

@app.get("/planning/", response_model=list[PlanningP])
async def get_all_planning_data(
    skip: int = Query(0, ge=0),
    limit_per_page: int = Query(10, le=100),
    sort_by: Optional[str] = Query(None, pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
    search_column: Optional[str] = None,
    search_query: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Planning)

    # Eager loading of related data
    query = query.options(joinedload(Planning.talent),
                          joinedload(Planning.skills),
                          joinedload(Planning.client),
                          joinedload(Planning.job))

    if sort_by is not None:
        query = query.order_by(getattr(Planning, sort_by))

    if search_query and search_column:
        column_to_filter = getattr(Planning, search_column)
        query = query.filter(column_to_filter == search_query)

    planning_data = query.offset(skip).limit(limit_per_page).all()

    return planning_data