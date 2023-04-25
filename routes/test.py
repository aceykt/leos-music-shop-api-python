from fastapi import APIRouter, Depends, status

from dependencies.segment import analytics_instance

router = APIRouter(
    prefix="/test",
    tags=["Test"],
    responses={404: {"description" : "Not found"}}
)

'''This is a test endpoint to test Segment sending specifically
an anonymous identify() call'''
@router.get("", status_code=status.HTTP_200_OK)
async def test_endpoint():
    analytics_instance.identify(
        anonymous_id='python-test-1234',
        traits={
            'first_name': 'Python',
            'last_name': 'Test',
        }
    )

    return {'Status': 'OK'}