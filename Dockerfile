FROM busybox:1.37.0
# FALCON's standard environment; no model, dataset or inference dependencies.
ENV PREDICTION_PATH=/submission/submission.csv \
    PREDICTION_PATH_LOCAL=/tmp/submission.pkl \
    GT_PATH=/tmp/ground_truth.pkl \
    EVAL_DATA_PATH=/dataset/evaluation_data \
    EVALUATION_LOC=remote SPLIT=m2 PHASE=test
# The marker proves the container started. Exit 42 is intentional, not a model error.
CMD ["sh", "-c", "echo FALCON_QUEUE_PROBE_STARTED; echo FALCON_QUEUE_PROBE_STARTED >&2; exit 42"]
